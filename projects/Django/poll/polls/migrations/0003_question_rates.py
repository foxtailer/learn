# Generated by Django 4.2.13 on 2024-07-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rate_questionrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rates',
            field=models.ManyToManyField(through='polls.QuestionRate', to='polls.rate'),
        ),
    ]