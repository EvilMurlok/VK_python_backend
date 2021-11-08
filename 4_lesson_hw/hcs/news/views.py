import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from application.settings import TEMPLATE_DIR
from .models import News


# render the page
def index(request):
    ordered_news = News.objects.all()
    return render(request, os.path.join(TEMPLATE_DIR, 'news/index.html'),
                  {'title': 'List of news', 'news': ordered_news})


# render the "read more" information
def view_news(request, news_id):
    try:
        news_item = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404('No News matches the given query.')
    return render(request, os.path.join(TEMPLATE_DIR, 'news/view_news.html'), context={'news_item': news_item,
                                                                                       'title': news_item.title})


# return the information about required news
def news_detail(request, news_id):
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404('No News matches the given query.')
    return JsonResponse({f'{news.title}': [f'{news.content}', f'{news.created_at}']})


def test(request):
    print(request)
    return HttpResponse('<h1>Test page!</h1>')
