from .import views
from django.urls import path


urlpatterns = [
    path('order/', views.OrderView.as_view(), name='order'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
]
