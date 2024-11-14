from django.db import models
from django.urls import reverse
from apps.common.model import BaseModel


class Logistic(BaseModel):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Nigeria")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Logistic"
        verbose_name_plural = "Logistics"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("logistic_detail", kwargs={"logistic_id": self.id})