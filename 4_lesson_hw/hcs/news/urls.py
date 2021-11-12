from django.urls import path
from .views import HomeNews
from .views import ViewNews
from .views import NewsByCategory
from .views import news_detail
from .views import add_news

urlpatterns = [
    path('', HomeNews.as_view(), name='news'),
    path('view_news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('add_news/', add_news, name='add_news')
]
