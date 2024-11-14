from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.forms import CustomUserChangeForm, CustomUserCreationForm

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_no",
                    "password1",
                    "password2",
                    "role",
                    "address",
                    "city",
                    "state",
                    "country",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "date_joined",
                ),
            },
        ),
    )
    form = CustomUserChangeForm
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                    "email",
                    "phone_no",
                    "role",
                    "address",
                    "city",
                    "state",
                    "country",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "password",
                    "user_permissions",
                    "date_joined",
                ),
            },
        ),
    )

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    readonly_fields = ("id",)
