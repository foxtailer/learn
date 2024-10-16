import json

from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Post, WiseUser


def home(request):
    context = {
        'page_title': 'Wise',
    }

    return render(request, 
                  'main/home.html',
                  context=context)


def write(request):
    if request.method == "POST":
        text = request.POST.get('text')
        answer = bool(request.POST.get('answer'))
        status = bool(request.POST.get('status'))
        user_id = request.user.id
        
        user = WiseUser.objects.get(id=user_id)

        Post.objects.create(text=text,
                            author=user,
                            reply=answer,
                            status=Post.Status.PUBLISHED if status else Post.Status.DRAFT
                            )
    
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
            'is_accepted': post.accepted.filter(id=user).exists(),
        }

        return JsonResponse(response_data)

    elif request.method == "PATCH":
        data = json.loads(request.body)

        post = Post.published.get(id=data.get('post_id'))
        user = WiseUser.objects.get(id=data.get('user_id'))
        is_accepted = data.get('is_accepted') == 'True' or data.get('is_accepted')

        if is_accepted:
            post.accepted.remove(user)
            post.save()
        else:
            post.accepted.add(user)
            post.save()

        response_data = {'status': '200',
                         'is_accepted': not is_accepted}
        return JsonResponse(response_data)
    
    elif request.method == "PUT":
        data = json.loads(request.body)

        post = Post.published.get(id=data.get('post_id'))
        user = WiseUser.objects.get(id=data.get('user_id'))
        
        post.report += 1
        post.reported_by.add(user)
        post.save()

        response_data = {'status': '200',}
        return JsonResponse(response_data)
    
    try:
        post = Post.random_wisdome(user=user)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    
    context = {
        'page_title': 'Explore',
        'post': post,
        'is_accepted': post.accepted.filter(id=user).exists(),
    }

    return render(request, 
                  'main/explore.html',
                  context=context)


def my(request):
    user_id = request.user.id
    #posts = Post.objects.filter(Q(accepted__id=user_id) & Q(author__id=user_id))
    posts1 = Post.objects.filter(accepted__id=user_id)
    posts2 = Post.objects.filter(author__id=user_id)
    posts = posts1 | posts2
    
    context = {'posts': posts,}

    return render(request,
                  'main/my.html',
                  context=context,)


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