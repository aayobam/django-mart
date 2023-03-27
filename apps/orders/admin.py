from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'tracking_no', 'status')
    search_fields = ('status', 'shipping_method', 'shipping_address')
    readonly_fields = ('total_price', 'tracking_no',)


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order',)