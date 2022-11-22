from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # template_name = 'app/time.html'
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'
    # return HttpResponse(msg)
    # context = {'current_time': current_time}
    # return render(request, template_name, context)
    return HttpResponse(msg)

def workdir_view(request):
    template_name = 'app/workdir.html'
    dirs = os.listdir(path='.')
    context = {'dirs': dirs}
    return render(request, template_name, context)
    # raise NotImplemented
