from .import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter(trailing_slash=False)

router.register('', views.VendorViewSet, basename='addresses')

urlpatterns = [
    path('', include(router.urls))
]
