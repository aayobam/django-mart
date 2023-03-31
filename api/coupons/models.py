from django.db import models
from django.urls import reverse
from api.common.models import TimeStampedModel


class Coupon(TimeStampedModel):
    code = models.CharField(max_length=10, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self) -> str:
        return self.code
    
    def get_absolute_url(self):
        return reverse("coupon_detail", kwargs={"coupon_id": self.id})
    
