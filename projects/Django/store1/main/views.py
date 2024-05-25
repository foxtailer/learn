from django.shortcuts import render
from goods.models import Categories

# Create your views here.

def index(request):
  categories = Categories.objects.all()

  context = {'title':'Home',
             'content':'HOME - главная.',
              'categories': categories
  }
  
  return render(request, 'main/index.html', context)

def about(request):
  context = {'title':'Home', 'content':'HOME - О нас.'}
  return render(request, 'main/about.html', context)
