import os

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import F
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect, render

from application.settings import TEMPLATE_DIR, LOGIN_URL
from .models import News, Category
from .forms import NewsForm


def login_required(view_func):
    def wrapped(request, *args, **kwargs):
        if request.user.is_anonymous:
            path = request.build_absolute_uri()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(path, LOGIN_URL)
        else:
            return view_func(request, *args, **kwargs)

    return wrapped


# this is an alternative and more convenient option of the function 'index'
class HomeNews(ListView):
    model = News
    template_name = os.path.join(TEMPLATE_DIR, 'news/home_news_list.html')
    context_object_name = 'news'
    # только для статичных данных! (для нестатичных переопределяется метод get_context_data
    extra_context = {'title': 'List of news'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'List of news'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = os.path.join(TEMPLATE_DIR, 'news/home_news_list.html')
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id']).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        news = News.objects.get(pk=self.kwargs['pk'])
        news.views = F('views') + 1
        news.save()
        context = super().get_context_data(**kwargs)
        return context


class CreateNews(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = NewsForm
    template_name = os.path.join(TEMPLATE_DIR, 'news/add_news.html')
    success_message = "News created successfully!"
    login_url = '/users/login/'


@login_required
@require_http_methods(["GET", "POST"])
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data) # тут содержится вся инфа по POST-запросу
            news = form.save()
            messages.success(request, 'News created successfully!')
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, os.path.join(TEMPLATE_DIR, 'news/add_news.html'),
                  context={'title': 'Add news', 'form': form})
