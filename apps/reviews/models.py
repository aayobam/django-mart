from django.db import models
from apps.users.models import CustomUser
from apps.products.models import Product
from apps.common.model import BaseModel
from apps.common.choice_helper import RATING_CHOICES


class Review(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews" )
    rating = models.IntegerField(choices=RATING_CHOICES)
    average_rating = models.FloatField(default=0.0)
    comment = models.TextField()

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return "Rating for " + self.product.name
    
    def get_absolute_url(self):
        return f"{self.id}"
