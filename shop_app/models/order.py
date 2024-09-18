from django.db import models

from shop_app.models.customer import Customer


class Order(models.Model):
    order_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')


    def __str__(self):
        return f'Order {self.id} {self.customer}'


    class Meta:
        ordering = ['-order_date']
        get_latest_by = 'order_date'



