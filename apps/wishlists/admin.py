from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class AdminWishlist(admin.ModelAdmin):
    list_display = ("user", "product")
