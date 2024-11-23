from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.user_cart, name='user_cart'),
    path('cart_add/<slug:product_slug>', views.cart_add, name='cart_add'),
    path('cart_remove/<slug:product_slug>/<slug:size>', views.cart_remove, name='cart_remove'),
    path('cart_change/<slug:product_slug>', views.cart_change, name='cart_change'),
]
