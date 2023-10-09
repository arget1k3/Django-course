from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]

from .models import *


def index(request):

    context =  {
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
        }
    
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:        
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_slug): 
    post = get_object_or_404(Women, slug=post_slug)

    context =  {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
        }

    return render(request, 'women/post.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_category(request, cat_slug):

    context =  {
        'menu': menu,
        'title': '',
        'cat_selected': cat_slug,
        }
    
    return render(request, 'women/index.html', context=context)