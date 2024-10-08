from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

from .models import Post


def home(request):
    
    context = {
        'page_title': 'Wise',
    }

    return render(request, 
                  'main/home.html',
                  context=context)


def write(request):
    return HttpResponse('wtite')
    #return render()


def explore(request):
    try:
        post = Post.random_wisdome()
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    
    context = {
        'page_title': 'Explore',
        'post': post,
    }
    
    return render(request, 
                  'main/explore.html',
                  context=context)


def my(request):
    return HttpResponse('my')
    #return render()


@require_POST
def report(request):
    post_id = request.POST.get('post_id')
    user = request.user
    try:
        wisdom = Post.published.get(id=post_id)
        wisdom.report += 1
        wisdom.reported_by.add(user)
        wisdom.save()
        return JsonResponse({'status': 'success', 'report': wisdom.report})
    except Post.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Wisdom not found'}, status=404)


@login_required
def logout(request):
  auth.logout(request)
  return redirect(reverse('main:home'))