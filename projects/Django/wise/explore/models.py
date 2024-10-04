from django.db import models
from main.models import User
#from taggit.managers import TaggableManager
import random
import string


# Function to generate a unique 6-character ID
# def generate_unique_id():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# class User(models.Model):
#     id = models.CharField(max_length=6, primary_key=True, default=generate_unique_id, editable=False)
#     birth_date = models.DateField()
#     password = models.CharField(max_length=128)  # Use appropriate hashing for passwords in practice
#     user_wisdom = models.ManyToManyField('Wisdom', related_name='users', blank=True)

#     def __str__(self):
#         return self.id

class Wisdom(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    text = models.TextField(max_length=1000, verbose_name='text')
    report = models.PositiveIntegerField(default=0, verbose_name='report')
    reported_by = models.ManyToManyField(User, related_name='reported_wisdoms', blank=True)
    accepted = models.ManyToManyField(User, related_name='accepted', blank=True)
    reply = models.BooleanField(default=True)
    #tags = TaggableManager(blank=True)

    @classmethod
    def wisdome_choice(cls):
        count = cls.objects.count()
        if count == 0:
            return None
        random_index = random.randint(0, count - 1)
        return cls.objects.all()[random_index]

        # wisdom_ids = cls.objects.values_list('id', flat=True)
        # if not wisdom_ids:
        #     return None
        # random_id = random.choice(wisdom_ids)
        # return cls.objects.filter(id=random_id).first()
    
    def __str__(self):
        return self.text[:10] + "..."

