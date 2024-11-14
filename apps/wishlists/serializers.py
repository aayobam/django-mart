from .models import Wishlist
from rest_framework import serializers


class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = "__all__"

    def update(self, instance, validated_data):
        instance =  super().update(instance, validated_data)
        instance.user = self.context.get("request").user
        instance.product = validated_data.get("product", instance.product)
        instance.save()
        return instance
    
    def validate(self, attrs):
        return super().validate(attrs)