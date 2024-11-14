from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ('id', 'user', 'session')
    readonly_fields = ('id',)


@admin.register(CartItem)
class AdminCartItem(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')
    readonly_fields = ('id',)