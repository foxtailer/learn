from django.db import models

from users.models import User
from goods.models import Product


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_prise() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, 
                             on_delete=models.CASCADE, 
                             verbose_name='User',
                             blank=True,
                             null=True)
    
    session_key = models.CharField(max_length=32,
                                   blank=True,
                                   null=True)
    
    product = models.ForeignKey(to=Product,
                                on_delete=models.CASCADE,
                                verbose_name='Product')
    
    quantity = models.PositiveSmallIntegerField(default=0,
                                                verbose_name='Quantity')
    
    created_timestamp = models.DateTimeField(auto_now_add=True,
                                             verbose_name='Date')
    
    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

    objects = CartQueryset().as_manager()

    def products_prise(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'
