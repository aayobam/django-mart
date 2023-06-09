from django.contrib import admin
from .models import Coupon


@admin.register(Coupon)
class AdminCoupon(admin.ModelAdmin):
    list_display = ("code", "discount", "valid_from", "valid_to", "active")
