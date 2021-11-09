from django.urls import path
from .views import user_detail
from .views import HomeUsers
# from .views import index

urlpatterns = [
    # path('', index, name='users'),
    path('', HomeUsers.as_view(), name='users'),
    path('user/', user_detail, name='current_user'),
]
