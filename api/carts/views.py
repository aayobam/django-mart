
from api.carts.models import Cart, CartItem
from api.products.models import Product
from .serializers import CartSerializer, CartItemSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.orders.models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAcceptable, ValidationError



class CreateCartView(generics.GenericAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        if request.user.is_authenticated:
            return Cart.objects.filter(user=request.user).first()
        else:
            session_key = request.session.session_key
            if not session_key:
                self.request.session.create()
                session_key = request.session.session_key
            return Cart.objects.filter(session=session_key).first()
        
    def create(self, serializer):
        data = serializer.validated_data.copy()
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if self.request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=self.request.user)
        else:
            session_key = self.request.session.session_key
            if not session_key:
                self.request.session.create()
                session_key = self.request.session.session_key
            cart, created = Cart.objects.get_or_create(session=session_key)

        cart_product, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        cart_product.quantity = quantity
        cart_product.save()
        serializer.instance = cart

    def perform_destroy(self, instance):
        data = self.request.data
        product_id = data.get('product_id')

        if instance:
            instance.products.filter(id=product_id).delete()
        return Response({'message': 'Cart cleared successfully.'}, status=status.HTTP_200_OK)


class CheckoutView(generics.GenericAPIView):
    def post(self, request):
        session = request.session.session_key
        cart = session.get('cart', {})
        for product_id, item in cart.items():
            product = Product.objects.get(id=product_id)
            product.inventory_count -= item['quantity']
            if product.inventory_count == 0:
                product.is_active = False
            product.save()
        session['cart'] = {}
        session.save()
        return Response({'message': 'Purchase completed successfully.'}, status=status.HTTP_200_OK)


