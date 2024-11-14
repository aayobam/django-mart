from django.db import models
from apps.users.models import CustomUser
from apps.common.model import BaseModel


class ShippingAddress(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="user_addresses")
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)

    class Meta:
        verbose_name = "User Address"
        verbose_name_plural = "User Addresses"

    def __str__(self) -> str:
        return 'Address for ' + self.user.email
