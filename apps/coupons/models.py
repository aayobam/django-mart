from django.db import models
from django.urls import reverse
from apps.common.model import BaseModel
from apps.vendors.models import Vendor


class Coupon(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="coupon")
    code = models.CharField(max_length=10, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

    class Meta:
        indexes =[
            models.Index(fields=["code"])
        ]
        ordering = ("-date_created",)
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    def __str__(self) -> str:
        return self.code
    
    def get_absolute_url(self):
        return reverse("coupon_detail", kwargs={"coupon_id": self.id})
    
