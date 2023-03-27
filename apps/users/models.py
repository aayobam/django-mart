from django.db import models
from django.urls import reverse
from apps.common import choice_helper
from apps.common.models import TimeStampedModel
from apps.users.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser, TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(default="male", choices=choice_helper.GENDER_CHOICES, max_length=10)
    role = models.CharField(default="admin", choices=choice_helper.ROLE_CHOICES, max_length=50)
    phone_no = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(default="nigeria", choices=choice_helper.COUNTRY_CHOICES, max_length=100)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    class Meta:
        ordering = ("-created_on",)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"user_id": self.id})
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
