from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Product

def main(request):
    products = Product.objects.all()

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)

    context = {'products': products,}

    return render(request, 'main/product.html', context)


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return HttpResponse(f'{product.name}')

def news(request):
    return render(request, 'main/news.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def social_plug(request):
    return render(request, 'social_plug.html')
