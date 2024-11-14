from .models import Category
from rest_framework import generics, viewsets
from .serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
