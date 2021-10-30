from django.urls import path
from .views import index
from .views import news_detail
from .views import test

urlpatterns = [
    path('', index),
    path('<int:news_id>', news_detail),
    path('test/', test),

]