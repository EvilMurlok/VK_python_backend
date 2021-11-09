from django.urls import path
from .views import HomeNews
from .views import ViewNews
from .views import NewsByCategory
from .views import news_detail
from .views import test
# from .views import view_news
# from .views import index

urlpatterns = [
    # path('', index, name='news'),
    # path('view_news/<int:news_id>/', view_news, name='view_news'),
    path('', HomeNews.as_view(), name='news'),
    path('view_news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('test/', test, name='test'),
]
