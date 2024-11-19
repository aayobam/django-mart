from django.db import models
from django.urls import reverse
from apps.common.model import BaseModel
from apps.users.models import CustomUser


class Logistic(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='logistic')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Nigeria")
    zip_code = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Logistic"
        verbose_name_plural = "Logistics"
        ordering = ("-date_created",)
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_logistic_name'),
        ]
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("logistic_detail", kwargs={"logistic_id": self.id})