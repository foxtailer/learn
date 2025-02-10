from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class Article(models.Model):
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")],
            verbose_name='заголовок'
    )
    text = models.TextField(verbose_name="текст")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="дата")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="обновлено")
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='рубрика',
                               related_name='articles')

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'
        ordering = ['-created_at']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name
 