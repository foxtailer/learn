from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='А ты прошел активацию?')
    send_messages = models.BooleanField(default=True,
                                       verbose_name='Слать...сообщения?')

    class Meta(AbstractUser.Meta):
        ...