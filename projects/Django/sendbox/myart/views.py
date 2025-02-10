from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Article, Rubric
from .forms import ArticleForm


def index(request):
    query = Article.objects.order_by('-id')
    rubrics = Rubric.objects.all()
    context = {'articles': query,
                               'rubrics': rubrics}
    return render(request, 'myart/index.html', context=context)


def my_rubric(request, rubric_id):
    query = Article.objects.filter(rubric__id=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=rubric_id)
    context = {'articles': query,
                               'rubrics': rubrics,
                               'current_rubric': current_rubric
                            }
    return render(request, 'myart/my_rubric.html', context=context)


class ArticleCreate(CreateView):
    template_name = 'myart/create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('my_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context