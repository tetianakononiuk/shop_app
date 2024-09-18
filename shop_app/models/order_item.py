from django.db import models

from shop_app.models import Product
from shop_app.models.order import Order


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'{self.quantity} x {self.product} for {self.order} '