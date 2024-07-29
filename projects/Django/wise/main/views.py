from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.forms import UserLoginForm


def main(request):
  return render(request, 'main/main.html')


def reg_log(request):
  form = UserLoginForm(data=request.POST)
  if form.is_valid():
    username = request.POST['username']  
    password = request.POST['password']  
    user = auth.authenticate(username=username, password=password)
    if user:
      auth.login(request, user)
      fail = False
      return HttpResponseRedirect(reverse('main:index'))
    
  fail = True
  form = UserLoginForm()
    
  context = {
    'fail': fail,
    'form': form,
  }

  return render(request, 'main/main.html', context)