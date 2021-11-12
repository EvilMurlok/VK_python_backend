import os
from django.db.models import F
from django.http import JsonResponse, Http404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods
from application.settings import TEMPLATE_DIR
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView
from django.contrib import messages


# this is an alternative and more convenient option of the function 'index'
class HomeNews(ListView):
    model = News
    template_name = os.path.join(TEMPLATE_DIR, 'news/home_news_list.html')
    context_object_name = 'news'
    # только для статичных данных! (для нестатичных переопределяется метод get_context_data
    extra_context = {'title': 'List of news'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'List of news'
        return context


class NewsByCategory(ListView):
    model = News
    template_name = os.path.join(TEMPLATE_DIR, 'news/home_news_list.html')
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id']).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        news = News.objects.get(pk=self.kwargs['pk'])
        news.views = F('views') + 1
        news.save()
        context = super().get_context_data(**kwargs)
        return context


# return the information about required news
@require_GET
def news_detail(request, news_id):
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404('No News matches the given query.')
    return JsonResponse({f'{news.title}': [f'{news.content}', f'{news.created_at}']})


@require_http_methods(["GET", "POST"])
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data) # тут содержится вся инфа по POST-запросу
            news = form.save()
            messages.success(request, 'Form submission successful')
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, os.path.join(TEMPLATE_DIR, 'news/add_news.html'),
                  context={'title': 'Add news', 'form': form})
