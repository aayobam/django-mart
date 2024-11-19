from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth", include("rest_framework.urls")),
    path("api/drivers/", include("apps.drivers.urls")),
    path("api/logistics/", include("apps.logistics.urls")),
    path("api/users/", include("apps.users.urls")),
    path("api/categories/", include("apps.categories.urls")),
    path("api/products/", include("apps.products.urls")),
    path("api/carts/", include("apps.carts.urls")),
    path("api/orders/", include("apps.orders.urls")),
    path("api/reviews/", include("apps.reviews.urls")),
    path("api/coupons/", include("apps.coupons.urls")),
    path("api/wishlists/", include("apps.wishlists.urls")),
    path("api/shipping/", include('apps.addresses.urls')),

    # Drf-spectacular open api
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "Django Mart Admin"
admin.site.site_header = "Django Mart Administrator"
