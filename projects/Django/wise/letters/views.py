from django.shortcuts import render
from django.http import HttpResponse

def letters(request):
  return HttpResponse('letters')