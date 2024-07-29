from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.main, name='index'),
  path('/reg-log', views.reg_log, name='reg-log'),
]