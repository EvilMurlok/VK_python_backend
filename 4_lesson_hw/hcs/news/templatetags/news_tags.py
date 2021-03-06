from django import template
from news.models import Category
import os
from application.settings import TEMPLATE_DIR
from django.db.models import Count, Q

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag(os.path.join(TEMPLATE_DIR, 'news/list_categories.html'))
def show_categories():
    # categories = Category.objects.filter(news__is_published=True).annotate(cnt=Count('news'))
    categories = Category.objects.annotate(cnt=Count('news', filter=Q(news__is_published=True))).filter(cnt__gt=0)
    return {'categories': categories}
