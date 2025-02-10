from django.urls import path

from .views import index, my_rubric, ArticleCreate


urlpatterns = [
    path('<int:rubric_id>', my_rubric, name='my_rubric'),
    path('add/', ArticleCreate.as_view(), name='add'),
    path('', index, name='my_list')
]

