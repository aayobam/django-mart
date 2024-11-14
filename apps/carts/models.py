from django.db import models
from apps.products.models import Product
from apps.users.models import CustomUser
from apps.common.model import BaseModel



class Cart(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='carts')
    session = models.CharField(max_length=255, null=True, blank=True)
    products = models.ManyToManyField(Product, through='CartItem', related_name='carts')

    class Meta:
        unique_together = ('user', 'session')
        ordering = ("-date_created",)
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"Cart " + str(self.id) + " for " + self.user.email


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='carts_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name + " " + str(self.quantity)
    