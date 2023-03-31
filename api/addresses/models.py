from django.db import models
from api.users.models import CustomUser
from api.common.models import TimeStampedModel


class ShippingAddress(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return 'Address for ' + self.user.email
