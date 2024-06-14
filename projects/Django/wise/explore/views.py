from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

from explore.models import Wisdom

# Create your views here.

def explore(request):
  # v 1
  # template = loader.get_template('explore.html')
  # return HttpResponse(template.render())

  wisdom = Wisdom.wisdome_choice()
  print(wisdom)
  context = {
    "wisdom": wisdom
  }
  return render(request, 'explore.html', context)
