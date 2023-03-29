from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ('user', 'products', 'cart_total_price')
    readonly_fields = ('id',)


@admin.register(CartItem)
class AdminCartItem(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'item_total_price')
    readonly_fields = ('id',)