from django.shortcuts import render

# Create your views here.

def index(request):
  context = {'title':'Home', 'content':'HOME - главная.'}
  return render(request, 'main/index.html', context)

def about(request):
  context = {'title':'Home', 'content':'HOME - О нас.'}
  return render(request, 'main/about.html', context)
