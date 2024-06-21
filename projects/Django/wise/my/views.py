from django.shortcuts import render

def my(request):
  return render(request, 'my/my.html')
