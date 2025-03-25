from django.shortcuts import render
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from carts.models import Cart


def login(request):
  if request.method == 'POST':
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
      username = request.POST['username']  
      password = request.POST['password']  
      user = auth.authenticate(username=username, password=password)
      
      session_key = request.session.session_key

      if user:
        auth.login(request, user)
        messages.success(request, f'{username}, Enter!')

        if session_key:
          Cart.objects.filter(session_key=session_key).update(user=user)

        redirect_page = request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
          return HttpResponseRedirect(request.POST.get('next'))
        return HttpResponseRedirect(reverse('main:home'))
  else:
    form = UserLoginForm()
    
  context = {
    'title': 'Home - login',
    'form': form,
  }

  return render(request, 'users/login.html', context)


def registration(request):
  if request.method == 'POST':
    form = UserRegistrationForm(data=request.POST)
    if form.is_valid():
      form.save()

      session_key = request.session.session_key

      user = form.instance
      auth.login(request, user)

      if session_key:
        Cart.objects.filter(session_key=session_key).update(user=user)
        
      return HttpResponseRedirect(reverse('main:home'))
  else:
    form = UserRegistrationForm()

  context = {
    'title': 'Home - registration',
    'form': form,
  }

  return render(request, 'users/registration.html', context)

@login_required
def profile(request):
  if request.method == 'POST':
    form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES )
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('user:profile'))
  else:
    form = ProfileForm(instance=request.user)

  context = {
    'title': 'Home - profile',
    'form': form,
  }

  return render(request, 'users/profile.html', context)


@login_required
def logout(request):
  auth.logout(request)
  messages.success(request, "HOHOHO!")
  return redirect(reverse('main:home'))


def users_cart(request):
  return render(request, 'users/user_cart.html')
