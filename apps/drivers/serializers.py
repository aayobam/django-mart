from rest_framework import serializers
from .models import Driver


class BasicDriverSerializer(serializers.Serializer):
    class Meta:
        model = Driver
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def validate(self, attrs):
        return super().validate(attrs)
