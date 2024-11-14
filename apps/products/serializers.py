from apps.products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_detail_url(self, obj):
        return obj.get_absolute_url()
