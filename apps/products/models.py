from django.db import models
from django.urls import reverse
from apps.categories.models import Category
from apps.common.model import BaseModel
from apps.vendors.models import Vendor


class Product(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("-date_created",)
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "Product"
        verbose_name_plural = "Products"


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_id": self.id})


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="products/images/")

    class Meta:
        ordering = ("-date_created",)
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return self.product.name + str(self.image)

    def get_absolute_url(self):
        return reverse("product_image", kwargs={"image_id": self.id})