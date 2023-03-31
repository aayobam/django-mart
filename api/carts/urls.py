from .import views
from django.urls import path


urlpatterns = [
    path("create", views.CreateCartView.as_view(), name="create_cart"),
]
