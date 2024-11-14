from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('', views.UserViewset, basename='users')

urlpatterns = [
    path("auth/", views.CustomTokenObtainPairView.as_view(), name="access_token"),
    path('', include(router.urls))
]
