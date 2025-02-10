from os import name
from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path('<str:page>/', views.other_page, name='other_page'),
    path('', views.index, name='index')
]
