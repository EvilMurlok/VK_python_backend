from django.urls import path, include

from .views import user_detail
from .views import HomeUsers
from .views import add_user
from .views import register_user
from .views import login_user
from .views import delete_user
from .views import logout_user
from .views import show_receipts

urlpatterns = [
    path('', HomeUsers.as_view(), name='users'),
    path('<int:pk>/', user_detail, name='current_user'),
    path('add_user/', add_user, name='add_user'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('delete_user/<int:pk>/', delete_user, name='delete_user'),
    path('logout/', logout_user, name='logout'),
    path('my_receipts/', show_receipts, name='show_receipts'),

]
