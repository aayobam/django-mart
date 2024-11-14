from .models import ShippingAddress
from rest_framework import generics, viewsets
from .serializers import ShippingAddressSerializer


class ShippingAddressList(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
        
