import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

from .models import Post, WiseUser


def home(request):
    context = {
        'page_title': 'Wise',
    }

    return render(request, 
                  'main/home.html',
                  context=context)


def write(request):
    return render(request,
                  'main/write.html')


def explore(request):
    user = request.user.id

    if request.method == "POST":
        except_id = request.POST.get('wisdom_id')
        post = Post.random_wisdome(except_id, user)

        response_data = {
            'wisdom': post.text,
            'wisdom_id': post.id,
            'reply': post.reply,
            'email': post.author.email,
        }

        return JsonResponse(response_data)

    elif request.method == "PATCH":
        data = json.loads(request.body)

        post = Post.published.get(id=data.get('post_id'))
        user = WiseUser.objects.get(id=data.get('user_id'))

        post.accepted.add(user)
        post.save()

        response_data = {'status': '200'}
        return JsonResponse(response_data)
    
    try:
        post = Post.random_wisdome(user=user)
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
    return render(request,
                  'main/my.html')


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