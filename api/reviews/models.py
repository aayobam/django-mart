from django.db import models
from api.users.models import CustomUser
from api.products.models import Product
from api.common.models import TimeStampedModel
from api.common.choice_helper import RATING_CHOICES


class Review(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

    def __str__(self) -> str:
        return "Rating for " + self.product.name
