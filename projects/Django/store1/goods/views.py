from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator
from goods.models import Products
# Create your views here.

def catalog(request, slug):

  if slug == "all":
    goods = Products.objects.all()
  else:
    goods = get_list_or_404(Products.objects.filter(category__slug=slug))

  p = Paginator(goods, 3)
  current_page = p.page(1)

  context = {
    'title': 'Home - Каталог',
    'goods': current_page
  }
  return render(request, 'goods/catalog.html', context)

def product(request, slug):

  product = Products.objects.get(slug=slug)

  context = {
    'product': product
  }

  return render(request, 'goods/product.html', context)