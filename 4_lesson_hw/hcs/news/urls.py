from django.urls import path
from .views import HomeNews
from .views import news_detail
from .views import test
from .views import view_news
# from .views import index

urlpatterns = [
    # path('', index, name='news'),
    path('', HomeNews.as_view(), name='news'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('view_news/<int:news_id>/', view_news, name='view_news'),
    path('test/', test, name='test'),
]
