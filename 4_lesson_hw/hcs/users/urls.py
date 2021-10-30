from django.urls import path
from .views import index
from .views import user_detail

urlpatterns = [
    path('', index),
    path('user/', user_detail),
]
