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
def report_wisdom(request):
    wisdom_id = request.POST.get('wisdom_id')
    try:
        wisdom = Wisdom.objects.get(id=wisdom_id)
        wisdom.report += 1
        wisdom.save()
        return JsonResponse({'status': 'success', 'report': wisdom.report})
    except Wisdom.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Wisdom not found'}, status=404)


def explore(request, wisdom_id=10):
  wisdom = Wisdom.objects.get(pk=wisdom_id)
  next = Wisdom.wisdome_choice().id
  context = {
    "wisdom": wisdom,
    "next": next,
  }

  return render(request, 'explore/explore.html', context)


@login_required
@require_POST
def accept_wisdom(request):
    wisdom_id = request.POST.get('wisdom_id')
    user = request.user
    
    try:
        wisdom = Wisdom.objects.get(id=wisdom_id)
        if user in wisdom.accepted.all():
            return JsonResponse({'status': 'error', 'message': 'Already accepted'}, status=400)

        wisdom.accepted.add(user)
        return JsonResponse({'status': 'success', 'accepted_count': wisdom.accepted.count()})
    except Wisdom.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Wisdom not found'}, status=404)