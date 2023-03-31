from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter
from api.common.custom_filter import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.common.custom_pagination import StandardResultsSetPagination


class CreateProductView(generics.CreateAPIView):
    """
    Product can only be added by an admin or superuser
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductListView(generics.ListAPIView):
    """
    You can search products by product name or category name
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    pagination_class = StandardResultsSetPagination
    search_fields = ["category__name", "name"]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(generics.UpdateAPIView):
    """
    Product can only be updated by an admin or superuser
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class DeleteProductView(generics.DestroyAPIView):
    """
    Product can only be deleted by an admin or superuser
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
