from .models import Coupon
from rest_framework import viewsets
from .serializers import CouponSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CouponViewset(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]