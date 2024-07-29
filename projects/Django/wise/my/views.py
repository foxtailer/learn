from django.shortcuts import render
from explore.models import Wisdom
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator


def my(request):
  wisdom = Wisdom.objects.all()
  paginator = Paginator(wisdom, 1)
  page_number = request.GET.get('wisdom', 1)
  posts = paginator.page(page_number)
  context = {
    'wisdom': posts
  }
  print( posts.has_next())
  return render(request, 'my/my.html', context)

@require_GET
def wisdom_prev(request):
    global n
    n -= 1
    wisdom = Wisdom.objects.all()[n]
    return JsonResponse({'wisdom': wisdom.text, 'n': n})

@require_GET
def wisdom_next(request):
    global n
    n += 1
    wisdom = Wisdom.objects.all()[n]
    return JsonResponse({'wisdom': wisdom.text, 'n': n})