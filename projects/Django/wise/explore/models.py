from django.db import models
import random

# Create your models here.

# class User(models.Model):
#   user = models.SlugField(max_length=6, unique=True, verbose_name='user')

class Wisdom(models.Model):
  # user = models.ForeignKey(to=User, on_delete=models.PROTECT, verbose_name='user')
  text = models.TextField(max_length=1000, verbose_name='text')
  report = models.PositiveIntegerField(default=0, verbose_name='report')

  @classmethod
  def wisdome_choice(cls):
      count = cls.objects.count()
      if count == 0:
          return None
      random_index = random.randint(0, count - 1)
      return cls.objects.all()[random_index].text
