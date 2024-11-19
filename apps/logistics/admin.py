from django.contrib import admin
from .models import Logistic


@admin.register(Logistic)
class AdminLogistic(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'country', 'zip_code', 'date_created', 'date_modified']
    readonly_fields = ['id', 'date_created', 'date_modified']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'email']