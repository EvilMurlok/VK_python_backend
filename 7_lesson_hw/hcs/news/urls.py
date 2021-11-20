from django.urls import path

from .views import NewsCreateView
from .views import NewsListView
from .views import NewsDetailView
from .views import NewsDetailByCategoryView
from .views import NewsUpdateView

urlpatterns = [
    path('create/', NewsCreateView.as_view(), name='create_news'),
    path('all/', NewsListView.as_view(), name='all_news'),
    path('current_news/<int:pk>/', NewsDetailView.as_view(), name='view_news'),
    path('category/<int:pk>/', NewsDetailByCategoryView.as_view(), name='by_category'),
    path('update/<int:pk>/', NewsUpdateView.as_view(), name='update_news'),

]
