from django.urls import path
from .views import UsersCreateView
from .views import UsersListView
from .views import UsersDeleteView
from .views import UsersUpdateUserInfoView
from .views import UserUpdateUsernameView
from .views import UserUpdatePasswordView

urlpatterns = [
    path('create/', UsersCreateView.as_view(), name='create_user'),
    path('all/', UsersListView.as_view(), name='all_users'),
    path('delete/<int:pk>/', UsersDeleteView.as_view(), name='delete_user'),
    path('update/username-info/<int:pk>/', UsersUpdateUserInfoView.as_view(), name='update_userinfo'),
    path('update/username/<int:pk>/', UserUpdateUsernameView.as_view(), name='update_username'),
    path('update/password/<int:pk>/', UserUpdatePasswordView.as_view(), name='update_password'),

]
