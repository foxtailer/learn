from django.db import models

from users.models import GaetaUser
from main.models import Product


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.product_price for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)

class Cart(models.Model):

    user = models.ForeignKey(to=GaetaUser, on_delete=models.CASCADE, verbose_name='User', blank=True, null=True)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Adding date')

    class Meta:
        db_table = 'cart'
    
    objects = CartQueryset().as_manager()

    def __str__(self):
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}' 
    
    def product_price(self):
        return round(self.product.price * self.quantity, 2)
