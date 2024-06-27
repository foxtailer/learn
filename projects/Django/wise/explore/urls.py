from django.urls import path
from explore import views

app_name = 'explore'

urlpatterns = [
    path('', views.explore, name='index'),
    path('get-random-wisdom/', views.get_random_wisdom, name='get_random_wisdom'),
    path('like/', views.like_wisdom, name='like'),
]
