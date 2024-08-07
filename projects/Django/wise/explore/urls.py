from django.urls import path
from explore import views

app_name = 'explore'

urlpatterns = [
    path('', views.explore, name='index'),
    path('<int:wisdom_id>/', views.explore, name='index'),
    path('accept_wisdom/', views.accept_wisdom, name='accept_wisdom'),
    path('get-random-wisdom/', views.get_random_wisdom, name='get_random_wisdom'),
    path('like/', views.report_wisdom, name='like'),
]
