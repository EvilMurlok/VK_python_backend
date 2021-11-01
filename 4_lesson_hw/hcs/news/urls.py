from django.urls import path
from .views import index
from .views import news_detail
from .views import test

urlpatterns = [
    path('', index, name='news'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('test/', test, name='test'),
]