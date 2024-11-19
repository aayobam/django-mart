from django.db import models
from apps.common.model import BaseModel
from django.urls import reverse
from apps.logistics.models import Logistic
from apps.users.models import CustomUser


class Driver(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='driver')
    logistic = models.ForeignKey(Logistic, on_delete=models.CASCADE, related_name='logistic_drivers')
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
        ordering = ("-date_created",)
        unique_together = ('user', 'logistic')
        constraints = [
            models.UniqueConstraint(fields=['user', 'logistic'], name='unique_driver_logistic'),
        ]
        
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("driver_detail", kwargs={"driver_id": self.id})