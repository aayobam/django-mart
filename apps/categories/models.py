from django.db import models
from django.urls import reverse
from apps.common.model import BaseModel
from apps.common.choice_helper import CATEGORY_CHOICES


class Category(BaseModel):
    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"category_id": self.id})
