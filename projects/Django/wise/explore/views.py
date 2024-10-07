from django.shortcuts import render, get_object_or_404
from explore.models import Wisdom
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required


@require_GET
def get_random_wisdom(request):
    random_wisdome = Wisdom.wisdome_choice()

    if random_wisdome:
        return JsonResponse({'wisdom': random_wisdome.text, 
                            'wisdom_id': random_wisdome.pk, 
                            'wisdom_author': random_wisdome.author.id,
                            'reply': random_wisdome.reply,})
    else:
        template = render_to_string('404.html')
        return HttpResponseNotFound(template)


@require_POST
def report_wisdom(request):
    wisdom_id = request.POST.get('wisdom_id')
    user = request.user
    try:
        wisdom = Wisdom.objects.get(id=wisdom_id)
        wisdom.report += 1
        wisdom.reported_by.add(user)
        wisdom.save()
        return JsonResponse({'status': 'success', 'report': wisdom.report})
    except Wisdom.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Wisdom not found'}, status=404)


def explore(request, wisdom_id=11):
  wisdom = Wisdom.objects.get(pk=wisdom_id)
  next = Wisdom.wisdome_choice().id
  reported_user_ids = wisdom.reported_by.values_list('id', flat=True)

  context = {
    "wisdom": wisdom,
    "next": next,
    "reported_by":reported_user_ids,
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