from apps.carts.models import Cart
from rest_framework import serializers
from apps.products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    cartitem_set = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = '__all__'