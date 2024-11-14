import random
from django.db import models
from django.urls import reverse
from apps.common import choice_helper
from apps.products.models import Product
from apps.users.models import CustomUser
from apps.common.model import BaseModel
from apps.addresses.models import ShippingAddress
from django.core.validators import MinValueValidator
from apps.common.choice_helper import PAYMENT_STATUS_CHOICES


class Order(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    coupon = models.CharField(max_length=10, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True, blank=True)
    tracking_no = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=20, choices=choice_helper.STATUS_CHOICES, default="pending")

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return f"Order {self.id} for {self.user.email}"

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"order_id": self.id})

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Item(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
