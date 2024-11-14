from django.urls import path, include
from .import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('', views.CouponViewset, basename='coupons')


urlpatterns = [
    path('', include(router.urls))
]
