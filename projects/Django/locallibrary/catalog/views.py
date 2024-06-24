from django.shortcuts import render

# Create your views here.

def catalog(request):
  context = {
    'gg': 123
  }
  return render(request, 'index0.html', context)