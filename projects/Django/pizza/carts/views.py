import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Cart
from main.models import Product


def user_cart(request):
    ...


def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    data = {'ingredient': request.POST.get('ingredient_0', None)}
    json_data = json.dumps(data)
    size = request.POST['size']

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += int(request.POST['quantity'])
                cart.save()
        else:
            Cart.objects.create(user=request.user,
                                product=product,
                                quantity=request.POST['quantity'],
                                size=size,
                                data=json_data)
        
    return HttpResponseRedirect(reverse('main:main'))


def cart_remove(request, product_slug):
    ...


def cart_change(request, product_slug):
    ...