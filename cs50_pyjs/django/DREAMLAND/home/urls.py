from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("general", views.general, name="General"),
    path("addition", views.addition, name="Addition")
]