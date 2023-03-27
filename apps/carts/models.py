from django.db import models
from apps.products.models import Product
from apps.users.models import CustomUser
from apps.common.models import TimeStampedModel


class Cart(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f'Cart for ' + self.user.email
    

class CartItem(TimeStampedModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'
