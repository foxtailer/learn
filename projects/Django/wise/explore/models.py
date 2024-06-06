from django.db import models

# Create your models here.

# class User(models.Model):
#   user = models.SlugField(max_length=6, unique=True, verbose_name='user')

class Wisdom(models.Model):
  # user = models.ForeignKey(to=User, on_delete=models.PROTECT, verbose_name='user')
  text = models.TextField(max_length=1000, verbose_name='text')
  report = models.PositiveIntegerField(default=0, verbose_name='report')