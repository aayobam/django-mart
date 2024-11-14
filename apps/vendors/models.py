from django.db import models
from apps.users.models import CustomUser
from apps.common.model import BaseModel


class Vendor(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor')
    vendor_code = models.CharField(max_length=32, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name
