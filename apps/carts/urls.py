from .import views
from django.urls import path



urlpatterns = [
    path('cart/', views.CreateCartView.as_view(), name='cart'),
]
