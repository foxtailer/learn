from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from explore.models import Wisdom
from main.models import User


def write(request):
  return render(request, 'write/write.html')

def addwise(request):
  text = request.POST['text']
  if text:
    reply = True if request.POST.get('answer', False) else False
    
    if request.POST['user'] == 'None':
      user = 1
    else:
      user = request.POST['user'] 

    wisdom = Wisdom(author=User.objects.get(id=user),
                    text=text, 
                    report=0, 
                    reply=reply)
    wisdom.save()
  return HttpResponseRedirect(reverse('write:index'))