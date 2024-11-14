from django.db import models
from apps.users.models import CustomUser
from apps.products.models import Product
from apps.common.model import BaseModel
from apps.common.choice_helper import RATING_CHOICES


class Review(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

    def __str__(self) -> str:
        return "Rating for " + self.product.name
