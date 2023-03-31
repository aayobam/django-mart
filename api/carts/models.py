from django.db import models
from api.products.models import Product
from api.users.models import CustomUser
from api.common.models import TimeStampedModel



class Cart(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    session = models.CharField(max_length=255, null=True, blank=True)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart " + str(self.id) + " for " + self.user.email


class CartItem(TimeStampedModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name + " " + str(self.quantity)
    