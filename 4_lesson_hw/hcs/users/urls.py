from django.urls import path
from .views import index
from .views import user_detail

urlpatterns = [
    path('', index, name='users'),
    path('user/', user_detail, name='current_user'),
]
