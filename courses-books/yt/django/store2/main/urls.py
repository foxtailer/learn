from django.urls import path, include
from . import views

app_name = 'name'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
]