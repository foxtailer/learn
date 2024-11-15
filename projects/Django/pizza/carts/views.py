from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Cart
from main.models import Product


def user_cart(request):
    ...


def cart_add(request, product_slug):
    try:
        print(request.POST['size'])
        print(request.POST['ingredient_0'])
        print(request.POST['quantity'])
    except:
        print("***")

    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        #carts = Cart.objects.filter(user=request.user, product=product)

        # if carts.exists():
        #     cart = carts.first()
        #     if cart:
        #         cart.quantity += 1
        #         cart.save()
        #     else:
        #Cart.objects.create(user=request.user, pro)
        ...
    return HttpResponseRedirect(reverse('main:main'))


def cart_remove(request, product_slug):
    ...


def cart_change(request, product_slug):
    ...