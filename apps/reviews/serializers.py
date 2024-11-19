from .models import Review
from rest_framework import serializers
from apps.products.models import Product
from django.shortcuts import get_object_or_404


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    
    def create(self, validated_data):
        product_id = self.kwargs.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        rating = validated_data.get("rating")
        average_rating = validated_data.get("average_rating")
        if rating == 0:
            validated_data["average_rating"] = 0
        validated_data["average_rating"] = (average_rating + rating) / 2
        validated_data['user'] = self.context['request'].user
        validated_data['product'] = product
        return super().create(validated_data)

    def validate(self, attrs):
        product_id = self.kwargs.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        user = self.context['request'].user
        review = self.Meta.model.objects.filter(user=user, product=product)
        if review.exists():
            raise serializers.ValidationError("You have already reviewed this product.")
        return super().validate(attrs)