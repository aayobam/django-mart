from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("auth/", views.CustomTokenObtainPairView.as_view(), name="access_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterUserApiView.as_view(), name="create_user"),
    path("all/", views.UserListApiView.as_view(), name="user_list"),
    path(
        "detail/<uuid:user_id>/", views.UserDetailApiView.as_view(), name="user_detail"
    ),
    path(
        "update/<uuid:user_id>/", views.UserUpdateApiView.as_view(), name="update_user"
    ),
    path(
        "delete/<uuid:user_id>/", views.UserDeleteApiView.as_view(), name="delete_user"
    ),
]
