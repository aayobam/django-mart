import random
from django.db import models
from django.urls import reverse
from api.common import choice_helper
from api.products.models import Product
from api.users.models import CustomUser
from api.common.models import TimeStampedModel
from api.addresses.models import ShippingAddress
from django.core.validators import MinValueValidator
from api.common.choice_helper import PAYMENT_STATUS_CHOICES


class Order(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True, blank=True)
    tracking_no = models.IntegerField()
    status = models.CharField(
        max_length=20, choices=choice_helper.STATUS_CHOICES, default="pending"
    )

    class Meta:
        ordering = ("-created_on",)

    def __str__(self):
        return f"Order {self.id} for {self.user.email}"

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"order_id": self.id})

    def save(self, *args, **kwargs):
        self.tracking_no = random.randint(0000000000, 9999999999)
        return super().save(*args, **kwargs)


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
