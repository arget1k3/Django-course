from django import template
from django.http import Http404
from women.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort = None, cat_selected = 0):
    if not sort:
        cats = Category.objects.all()
    else:   
        cats = Category.objects.order_by(sort) 

    return {'cats': cats, 'cat_selected': cat_selected}

@register.simple_tag(name='getposts')
def get_posts(filter=None):
    if not filter:
        return Women.objects.all()
    else:
        return Women.objects.filter(cat_id=filter)

@register.inclusion_tag('women/list_posts.html')
def show_posts(filter=None):
    if not filter:
        posts = Women.objects.all()
    else:
        filter = 1 if filter == 'aktrisy' else 2 ##crutch
        posts = Women.objects.filter(cat_id=filter)  

    if len(posts) == 0:
        raise Http404    

    return {'posts': posts}       


