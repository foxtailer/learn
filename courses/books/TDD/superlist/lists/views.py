from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text', ''))
        return redirect('/lists/the-only-list-in-the-world/')
    else:

    # context = {
    #     'new_item_text': new_item_text
    # }
    # return HttpResponse(request.POST['item_text'])
        items = Item.objects.all()
        return render(request, 'lists/home.html', {'items':items})


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items': items})