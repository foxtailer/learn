from django.shortcuts import render, get_object_or_404
from explore.models import Wisdom, User
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

# Create your views here.

@require_GET
def get_random_wisdom(request):
    random_wisdome = Wisdom.wisdome_choice()  # Assuming get_random is a class method
    return JsonResponse({'wisdom': random_wisdome.text, 'wisdom_id': random_wisdome.pk})

@require_POST
def add_wisdom(request):
    wisdom_id = request.POST.get('wisdom_id')
    user_id = request.POST.get('user_id')  # This should come from your session or user authentication
    user = get_object_or_404(User, id=user_id)
    wisdom = get_object_or_404(Wisdom, id=wisdom_id)
    user.user_wisdom.add(wisdom)
    return JsonResponse({'status': 'success'})

def explore(request):
  wisdom = Wisdom.wisdome_choice()
  context = {
    "wisdom": wisdom
  }

  return render(request, 'explore/explore.html', context)
