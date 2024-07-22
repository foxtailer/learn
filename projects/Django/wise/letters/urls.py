from django.urls import path
from letters import views

app_name = 'letters'

urlpatterns = [
    path('', views.letters, name='index'),
]