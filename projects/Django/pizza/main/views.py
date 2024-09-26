from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product

def main(request):
    products = Product.objects.all()

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)

    return render(request, 'main/product.html', {'products': products})


def news(request):
    return render(request, 'main/news.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def social_plug(request):
    return render(request, 'social_plug.html')
