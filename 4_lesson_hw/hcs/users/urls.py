from django.urls import path
from .views import user_detail
from .views import HomeUsers
from .views import add_user
from .views import register
from .views import login
from .views import delete_user

urlpatterns = [
    path('', HomeUsers.as_view(), name='users'),
    path('<int:pk>/', user_detail, name='current_user'),
    path('add_user/', add_user, name='add_user'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('delete_user/<int:pk>/', delete_user, name='delete_user'),
]
