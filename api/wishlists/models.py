from django.db import models
from api.users.models import CustomUser
from api.products.models import Product
from api.common.models import TimeStampedModel


class Wishlist(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
