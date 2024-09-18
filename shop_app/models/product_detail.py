from django.db import models
from .category import Category
from .supplier import Supplier

from .product import Product

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='details')
    description = models.TextField(null=True, blank=True)
    manufacturing_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f'Details of {self.product}'


