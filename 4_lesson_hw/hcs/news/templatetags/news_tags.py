from django import template
from news.models import Category
import os
from application.settings import TEMPLATE_DIR

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag(os.path.join(TEMPLATE_DIR, 'news/list_categories.html'))
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
