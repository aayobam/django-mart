from .models import Product
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter
from apps.common.custom_filter import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.common.custom_pagination import StandardResultsSetPagination
from rest_framework.decorators import action


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    pagination_class = StandardResultsSetPagination
    search_fields = ["category__name", "name"]

    def get_paginated_result(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_serializer_class(self):
        return super().get_serializer_class()
    
    def get_permissions(self):
        return super().get_permissions()