# Generated by Django 4.2 on 2024-11-20 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
