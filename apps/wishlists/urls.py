from .import views
from rest_framework import routers
from django.urls import path, include

routers = routers.DefaultRouter(trailing_slash=False)
routers.register('', views.WishlistViewset, basename='wishlists')


urlpatterns = [
    path('', include(routers.urls))
]
