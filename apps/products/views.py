from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.common.custom_pagination import StandardResultsSetPagination


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
    search_fields = ["name", "category__name"]
    filter_backends = [filters.SearchFilter]
    pagination_class = StandardResultsSetPagination

    
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