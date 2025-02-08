from django.shortcuts import render
from django.http import HttpResponse


from .models import Article


def index(request):
    query = Article.objects.order_by('-id')
    context = {'articles': query}
    return render(request, 'myart/index.html', context=context)

