from rest_framework import serializers
from .models import ShippingAddress



class ShippingAddressSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    class Meta:
        model = ShippingAddress
        fields = '__all__'