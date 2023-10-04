from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def categories(request, catid):
    if(request.POST):
        print(request.POST) # http://127.0.0.1:8000/cats/1/?name=Gagarina&type=pop
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if int(year)>2023:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Архив по городам</h1><p>{year}</p>') # http://127.0.0.1:8000/archive/2023/

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')