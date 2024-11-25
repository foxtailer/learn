import json

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse

from .models import Product
from .forms import CategoryFilterForm


def main(request):
    form = CategoryFilterForm(request.GET or None)
    products = Product.objects.all()

    selected_categories = [1,2,3]
    if request.method == 'GET' and form.is_valid():
        selected_categories.clear()
        for key, value in form.cleaned_data.items():
            if value:  # Checkbox is checked
                category_id = key.split('_')[1]  # Extract category ID from the key
                selected_categories.append(int(category_id))
        if selected_categories:
            products = products.filter(category__in=selected_categories)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
    form = CategoryFilterForm(selected_categories=selected_categories)

    context = {'products': products,
               'form': form,
               'title': 'Gaeta Pizza'}

    return render(request, 'main/product.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    return HttpResponse(f'{product.name}')


def news(request):
    context = {
        'title': 'News'
    }
    return render(request, 'main/news.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'Contacts'
    }
    return render(request, 'main/contacts.html', context)


def social_plug(request):
    return render(request, 'social_plug.html')


def update_rating(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            body = json.loads(request.body)
            user_rating = int(body.get('userRating'))
            product_id = int(body.get('productId'))
            
            product = Product.objects.get(id=product_id)
            new_rating = product.update_rating(user_rating)

            # Return the new rating as a JSON response
            return JsonResponse({'newRating': new_rating}, status=200)
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            return JsonResponse({'error': 'Invalid input'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
