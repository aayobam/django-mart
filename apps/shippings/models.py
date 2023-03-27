from django.db import models
from apps.common.models import TimeStampedModel

# Create your models here.
class Shipping(TimeStampedModel):
    name = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_delivery = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.method}"