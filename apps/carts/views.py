from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from .serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from apps.products.models import Product


class CartView(generics.GenericAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        serializer = self.serializer_class(cart.cartitem_set.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, id=request.data['product'])
        cart_item = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += int(request.data.get('quantity', 1))
        cart_item.save()
        serializer = self.serializer_class(cart.cartitem_set.all(), many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        cart_item = get_object_or_404(CartItem, id=id, cart__user=request.user)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)