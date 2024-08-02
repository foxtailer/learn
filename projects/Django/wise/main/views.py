from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from main.forms import UserLoginForm, UserRegistrationForm


def main(request):
  fail = request.GET.get('fail', 'False') == "True"

  context = {
    'fail': fail,
  }

  return render(request, 'main/main.html', context)


def login(request):
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
    
  context = {
    'fail': fail,
    'form': form,
  }

  return render(request, 'main/main.html', context)


def registration(request):
  if request.method == 'POST':
    form = UserRegistrationForm(data=request.POST)
    if form.is_valid():
      form.save()
      user = form.instance
      auth.login(request, user)
      return HttpResponseRedirect(reverse('main:index'))
  else:
    form = UserRegistrationForm()

  context = {
    'form': form,
  }

  return render(request, 'main/registration.html', context)

@login_required
def logout(request):
  auth.logout(request)
  return redirect(reverse('main:index'))
