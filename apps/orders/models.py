import random
from django.db import models
from apps.common import choice_helper
from apps.products.models import Product
from apps.users.models import CustomUser
from apps.common.models import TimeStampedModel


class Order(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.CharField(max_length=255, blank=True)
    tracking_no = models.IntegerField()
    status = models.CharField(max_length=20, choices=choice_helper.STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f"Order {self.id} for {self.user.email}"
    
    def save(self, *args, **kwargs):
        self.tracking_no = random.randint(0000000000,9999999999)
        return super().save(*args, **kwargs)


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'