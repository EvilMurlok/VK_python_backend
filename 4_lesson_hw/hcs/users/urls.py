from django.urls import path
from .views import user_detail
from .views import HomeUsers
from .views import add_user

urlpatterns = [
    path('', HomeUsers.as_view(), name='users'),
    path('<int:pk>/', user_detail, name='current_user'),
    path('add_user/', add_user, name='add_user'),
]
