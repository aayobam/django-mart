from django.db import models
from django.urls import reverse
from apps.users.models import CustomUser
from apps.products.models import Product
from apps.common.model import BaseModel


class Wishlist(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-date_created",)
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
        unique_together = ("user", "product")

    def __str__(self):
        return self.user.get_full_name() + " " + self.product.name
    
    def get_absolute_url(self):
        return reverse("wish_detail", kwargs={"id": self.id})
    
