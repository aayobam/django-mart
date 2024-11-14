from rest_framework import serializers
from apps.products.models import Product
from apps.carts.models import Cart, CartItem
from apps.addresses.serializers import ShippingAddressSerializer


# Created specifically for CartItem operations only. not to be used on views.
class SimpleProductserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    products = SimpleProductserializer(many=True)
    sub_total = serializers.SerializerMethodField(method_name="get_sub_total")

    class Meta:
        fields = ['id', 'cart', 'products', 'quantity', 'sub_total']

    def total(self, cartitem:CartItem):
        sum_total = cartitem.product.price * cartitem.quantity
        return sum_total


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    products = CartItemSerializer(many=True)
    grand_total = serializers.SerializerMethodField(method_name='get_grand_total_amount')
    shipping_address = ShippingAddressSerializer()
    
    class Meta:
        model = Cart
        fields = "__all__"
    
    def get_grand_total_amount(self, cart:Cart):
        products = cart.items.all()
        total_amount = sum([product.sub_total for product in products])
        return total_amount