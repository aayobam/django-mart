from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'image')
    readonly_fields = ('id',)
    search_fields = ('name', 'category__name')
