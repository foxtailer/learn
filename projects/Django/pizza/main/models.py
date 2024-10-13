from django.db import models
from django.urls import reverse

    
class Categories(models.Model):
    name = models.CharField(max_length=150,
                            unique=True,
                            verbose_name='Category')
    
    slug = models.SlugField(max_length=200,
                            unique=True,
                            blank=True,
                            null=True,
                            verbose_name='URL')

    class Meta():
        db_table = 'category'

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=150,
                            unique=True,
                            verbose_name='Name')
    
    slug = models.SlugField(max_length=200,
                            unique=True,
                            blank=True,
                            null=True,
                            verbose_name='URL')
    
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name='Description')
    
    image = models.ImageField(upload_to='goods_images',
                              blank=True,
                              null=True,
                              verbose_name='Image')
    
    price = models.DecimalField(default=0,
                                max_digits=7,
                                decimal_places=2,
                                verbose_name='Price')
    
    category = models.ForeignKey(to=Categories,
                                 on_delete=models.PROTECT)
    
    ingredients = models.ManyToManyField(Ingredient,
                                         related_name='products',
                                         blank=True)
    
    def get_absolute_url(self):
        return reverse('main:product',
                       args=[self.id])
    