from decimal import Decimal

from django.db import models

from users.models import GaetaUser
from main.models import Product


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.product_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)


class Cart(models.Model):
    class Size(models.TextChoices):
        SMALL = 'S', 'Small'
        MEDIUM = 'M', 'Medium'
        LARGE = 'L', 'Large'

    user = models.ForeignKey(to=GaetaUser, on_delete=models.CASCADE, verbose_name='User', blank=True, null=True)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    data = models.JSONField()
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Adding date') 
    size = models.CharField(max_length=1,
                              choices=Size.choices,
                              default=Size.MEDIUM)
    class Meta:
        db_table = 'cart'
    
    objects = CartQueryset().as_manager()

    def __str__(self):
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}' 
    
    def product_price(self):
        if self.size == 'S':
            return (self.product.price * Decimal('0.8')) * self.quantity
        if self.size == 'M':
            return self.product.price * self.quantity
        if self.size == 'L':
            return (self.product.price * Decimal(1.2)) * self.quantity
