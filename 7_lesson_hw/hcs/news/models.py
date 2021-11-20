from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    content = models.TextField(blank=True, verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Category')
    views = models.IntegerField(default=0, verbose_name='views')
    is_published = models.BooleanField(default=True, verbose_name='is_published')

    # def get_absolute_url(self):
    #     return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Category_name')

    # def get_absolute_url(self):
    #     return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
