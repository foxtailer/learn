from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class GaetaUser(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    phone_number = PhoneNumberField()
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return self.username
