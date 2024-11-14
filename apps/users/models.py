from django.db import models
from django.urls import reverse
from apps.common import choice_helper
from apps.common.model import BaseModel
from apps.users.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def validated_phone_no(value):
    if len(value) < 11 or len(value) > 11:
        raise ValidationError("phone number cannot be higher or less than 11")
    if type(value) != int:
        raise ValidationError("phone number should be whole number")


class CustomUser(AbstractUser, BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(default="admin", choices=choice_helper.ROLE_CHOICES, max_length=50)
    phone_no = models.CharField(max_length=11, validators=[validated_phone_no])

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("-date_created",)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"user_id": self.id})