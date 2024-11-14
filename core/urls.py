from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Django Mart E Commerce Store",
        default_version="v1",
        description="Ecommerce web app documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="aayobam@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-view/", include("rest_framework.urls")),
    path("api/users/", include("apps.users.urls")),
    path("api/categories/", include("apps.categories.urls")),
    path("api/products/", include("apps.products.urls")),
    path("api/carts/", include("apps.carts.urls")),
    path("api/orders/", include("apps.orders.urls")),
    path("api/reviews/", include("apps.reviews.urls")),
    path("api/coupons/", include("apps.coupons.urls")),
    path("api/wishlists/", include("apps.wishlists.urls")),
    path("api/shipping/", include('apps.addresses.urls')),

    # Drf-yasg open api
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("swagger.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "Django Mart Admin"
admin.site.site_header = "Django Mart Administrator"
