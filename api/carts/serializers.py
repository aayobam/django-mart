from rest_framework import serializers
from api.products.models import Product
from api.carts.models import Cart, CartItem
from api.orders.models import Order, OrderItem
from api.addresses.models import ShippingAddress
from api.products.serializers import ProductSerializer
from api.addresses.serializers import ShippingAddressSerializer


# Created specifically for CartItem operations only. not to be used on views.
class SimpleProductserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductserializer(many=False)
    sub_total = serializers.SerializerMethodField(method_name="get_sub_total")

    class Meta:
        fields = ['id', 'cart', 'product', 'quantity', 'sub_total']

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
        #total_amount = sum([item.product.price * item.quantity for item in products])
        return total_amount