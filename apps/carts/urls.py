from .import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter(trailing_slash=False)
router.register('', views.CartViewSet, basename='cart')


urlpatterns = [
    path('', include(router.urls))
]
