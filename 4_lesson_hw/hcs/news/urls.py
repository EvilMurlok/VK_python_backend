from django.urls import path
from .views import HomeNews
from .views import ViewNews
from .views import CreateNews
from .views import NewsByCategory
# from .views import add_news

urlpatterns = [
    path('', HomeNews.as_view(), name='news'),
    path('view_news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('add_news/', add_news, name='add_news'),
    path('add_news/', CreateNews.as_view(), name='add_news'),
]
