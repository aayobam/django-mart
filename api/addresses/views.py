from .models import ShippingAddress
from rest_framework import generics
from .serializers import ShippingAddressSerializer


class ShippingAddressList(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

    def get_queryset(self):
        user = self.request.user
        return ShippingAddress.objects.filter(user=user)
        
