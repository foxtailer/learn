from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('home!')

def general(request):
    return HttpResponse('General')

def addition(request):
    return HttpResponse('Addition')