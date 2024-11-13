from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm


def login(request):
    form = UserLoginForm(data=request.POST)

    if form.is_valid:
        username = request.POST['username']  
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Please correct the errors below.")

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/"
    return HttpResponseRedirect(next_url)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:main'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Register',
        'form': form,
    }

    return render(request, 'users/register.html', context)


def profile(request):
    context = {
        'title': 'Profile'
    }

    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/"
    return HttpResponseRedirect(next_url)
