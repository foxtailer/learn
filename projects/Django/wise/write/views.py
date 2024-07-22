from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from explore.models import Wisdom
from django.contrib.auth.models import User


def write(request):
  return render(request, 'write/write.html')

def addwise(request):
  #return HttpResponse('gg')
  text = request.POST['text']
  wisdom = Wisdom(author=User.objects.get(id=1),text=text, report=0)
  wisdom.save()
  return HttpResponseRedirect(reverse('write:index'))