from . import views
from django.urls import path


urlpatterns = [
    path("list", views.OrderView.as_view(), name="order_list"),
    path(
        "details/<uuid:order_id>", views.OrderListView.as_view(), name="order_details"
    ),
]
