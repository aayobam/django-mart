from .models import Coupon
from rest_framework import generics
from .serializers import CouponSerializer


class CreateCouponView(generics.CreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponListView(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponDetailView(generics.RetrieveAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class UpdateCouponView(generics.UpdateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

