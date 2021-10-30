import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from application.settings import TEMPLATE_DIR
from .models import Users


# render the page
def index(request):
    ordered_news = Users.objects.order_by('-created_at')
    return render(request, os.path.join(TEMPLATE_DIR, 'users/index.html'),
                  {'title': 'Список новостей', 'news': ordered_news})


def news_detail(request, news_id):
    try:
        news = Users.objects.get(pk=news_id)
    except:
        raise Http404
    return JsonResponse({f'{news.title}': [f'{news.content}', f'{news.created_at}']})


def test(request):
    print(request)
    return HttpResponse('<h1>Test page!</h1>')
