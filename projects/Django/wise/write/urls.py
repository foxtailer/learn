from django.urls import path
from write import views

app_name = 'write'

urlpatterns = [
    path('', views.write, name='index'),
    path('addwise/', views.addwise, name='addwise'),
]