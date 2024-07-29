from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser

class UserLoginForm(AuthenticationForm):
  username = forms.CharField() 
  password = forms.CharField()

  class Meta:
    model = AbstractUser