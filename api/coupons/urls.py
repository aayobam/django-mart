from django.urls import path
from .import views


urlpatterns = [
    path("create/", views.CreateCouponView.as_view(), name="create_coupon"),
    path("list/", views.CouponListView.as_view(), name="coupon_list"),
    path("detail/<uuid:copoun_id>", views.CouponDetailView.as_view(), name="coupon_detail"),
    path("update/<uuid:copoun_id>", views.UpdateCouponView.as_view(), name="update_coupon")
]
