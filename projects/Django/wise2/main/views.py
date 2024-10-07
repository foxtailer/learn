from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'title': 'wise',
    }
    return render(request, 
                  'main/home.html',
                  context=context)


def write(request):
    return HttpResponse('wtite')
    #return render()


def explore(request):
    return HttpResponse('explore')
    #return render()


def my(request):
    return HttpResponse('my')
    #return render()