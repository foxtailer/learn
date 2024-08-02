from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
  path('', views.main, name='index'),
  path('login/', views.login, name='login'),
  path('registration/', views.registration, name='registration'),
  path('logout/', views.logout, name='logout'),
]