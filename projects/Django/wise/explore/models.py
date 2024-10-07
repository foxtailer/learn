import random

from django.db import models
from django.shortcuts import get_object_or_404
from main.models import User


class Wisdom(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    text = models.TextField(max_length=1000, verbose_name='text')
    report = models.PositiveIntegerField(default=0, verbose_name='report')
    reported_by = models.ManyToManyField(User, related_name='reported_wisdoms', blank=True)
    accepted = models.ManyToManyField(User, related_name='accepted', blank=True)
    reply = models.BooleanField(default=True)

    @classmethod
    def wisdome_choice(cls):
        count = cls.objects.count()
        if count == 0:
            return None
        random_index = random.randint(0, count - 1)
        return cls.objects.all()[random_index]
    
    def __str__(self):
        return f'({self.author}) {self.text[:10]}...'

