from rest_framework import viewsets
from .serializers import VendorSerializer
from .models import Vendor
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]