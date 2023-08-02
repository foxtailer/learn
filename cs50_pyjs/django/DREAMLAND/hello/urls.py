from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page1", views.page1, name="Eva"),
    path("page2", views.page2, name="Zoy"),
    path("<str:name>", views.greet, name="greet"),
    path("main", views.main, name="main")
]