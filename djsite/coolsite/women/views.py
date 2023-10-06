from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]

from .models import *


def index(request):
    posts = Women.objects.all()
    context =  {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
        }
    
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id={post_id}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')