# Bu yerda kategoriyalarni ishlatish uchun sslilka yaratiladi
from django import template
from django.db.models import Count
from blog.models import Category, Article

register = template.Library()


@register.simple_tag()
def get_all_categories():
    categoreies = Category.objects.annotate(Count('article'))
    return categoreies

