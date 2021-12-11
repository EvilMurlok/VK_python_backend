from django.contrib import admin
from .models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category', 'views', 'is_published')
    list_display_links = ('id', 'title', 'views')
    list_editable = ('is_published',)
    search_fields = ('title', 'category',)
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
