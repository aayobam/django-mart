from django.urls import path
from .import views


urlpatterns = [
    path('address/list', views.ShippingAddressList.as_view(), name='shipping_address_list'),
]
