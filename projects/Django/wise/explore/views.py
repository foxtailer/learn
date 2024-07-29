from django.shortcuts import render, get_object_or_404
from explore.models import Wisdom
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.

@require_GET
def get_random_wisdom(request):
    random_wisdome = Wisdom.wisdome_choice()  # Assuming get_random is a class method
    #tags = [tag.name for tag in random_wisdome.tags.all()]
    return JsonResponse({'wisdom': random_wisdome.text, 
                        'wisdom_id': random_wisdome.pk, 
                        'wisdom_author': random_wisdome.author.id,
                        #'tag': tags,
                        'reply': random_wisdome.reply,})


@require_POST
def like_wisdom(request):
    # wisdom_id = request.POST.get('wisdom_id')
    # wisdom = get_object_or_404(Wisdom, id=wisdom_id)
    # wisdom.accepted.add(request.user)
    # return JsonResponse({'status': 'liked', 'quote_id': wisdom_id})
    return HttpResponse('gg')

def explore(request):
  wisdom = Wisdom.wisdome_choice()
  context = {
    "wisdom": wisdom
  }

  return render(request, 'explore/explore.html', context)
