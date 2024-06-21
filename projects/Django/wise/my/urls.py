from django.urls import path
from my import views

app_name = 'my'

urlpatterns = [
    path('', views.my, name='index'),
]