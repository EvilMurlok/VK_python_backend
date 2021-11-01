from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at')
    list_display_links = ('id', 'title', 'content')
    search_fields = ('title', 'content')


admin.site.register(News, NewsAdmin)
