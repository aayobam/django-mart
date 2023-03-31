from django.contrib import admin
from .models import ShippingAddress


@admin.register(ShippingAddress)
class AdminShippingAddress(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('city', 'state')
