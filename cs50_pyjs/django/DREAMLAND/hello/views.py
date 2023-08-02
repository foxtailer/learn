from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/hello.html')

def page1(request):
    return HttpResponse('Hello Eva')

def page2(request):
    return HttpResponse('Hello Zoy')

def greet(request, name):
    return HttpResponse(f'Hello, {name.capitalize()}')

def main(request):
    return render(request, 'hello/main.html')

