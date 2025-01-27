from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    # Все типы полей находятся на странице
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    
    # перечисляемый класс Status путем подклассирования
    # класса models.TextChoices. Доступными вариантами статуса поста являются
    # DRAFT и PUBLISHED. Их соответствующими значениями выступают DF и PB, а их
    # метками или читаемыми именами являются Draft и Published.
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # транслируется в столбец DATE­TIME в базе данных SQL
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    tags = TaggableManager()

    class Meta:
        # определим
        # заранее заданный порядок. Он будет применяться при извлечении объектов
        # из базы данных, в случае если в запросе порядок не будет указан.
        ordering = ['-publish']
        # Индекс повысит
        # производительность запросов, фильтрующих или упорядочивающих резуль-
        # таты по указанному полю. Мы ожидаем, что многие запросы извлекут пре-
        # имущества из этого индекса, поскольку для упорядочивания результатов мы
        # по умолчанию используем поле publish.
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
