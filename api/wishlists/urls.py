from django.urls import path
from .import views


urlpatterns = [
    path("wishlist/", views.WishlistListView.as_view(), name="wishlist_list"),
]
