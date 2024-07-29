from django.urls import path
from my import views

app_name = 'my'

urlpatterns = [
    path('', views.my, name='index'),
    path('wisdom_prev', views.wisdom_prev, name='wisdom_prev'),
    path('wisdom_next', views.wisdom_next, name='wisdom_next'),
]