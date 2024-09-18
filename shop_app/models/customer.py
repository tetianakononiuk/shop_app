from django.db import models

from config.settings import TEMPLATES
from .category import Category
from .supplier import Supplier
from .address import Address


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.OneToOneField('Address', null=True, blank=True, on_delete=models.SET_NULL, related_name='customer')
    date_joined = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-date_joined']
        get_latest_by = 'date_joined'
