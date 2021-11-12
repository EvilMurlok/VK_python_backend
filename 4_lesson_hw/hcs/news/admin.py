from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'category', 'views')
    list_display_links = ('id', 'title', 'content', 'views')
    search_fields = ('title', 'content', 'category',)
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
