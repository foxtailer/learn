from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('social-plug/', views.social_plug, name='social_plug'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('update-rating/', views.update_rating, name='update_rating'),
]
