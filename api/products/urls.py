from . import views
from django.urls import path


urlpatterns = [
    path("create/", views.CreateProductView.as_view(), name="create_product"),
    path("list/", views.ProductListView.as_view(), name="product_list"),
    path(
        "detail/<uuid:product_id>",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "update/<uuid:product_id>",
        views.UpdateProductView.as_view(),
        name="update_product",
    ),
    path(
        "delete/<uuid:product_id>",
        views.DeleteProductView.as_view(),
        name="delete_product",
    ),
]
