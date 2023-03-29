from .models import Cart
from rest_framework import status
from rest_framework import generics
from .serializers import CartSerializer
from apps.products.models import Product
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



class CreateCartView(generics.CreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        serializer = self.serializer_class(cart.cartitem_set.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, id=request.data['product_id'])
        cart_item = Cart.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += int(request.data.get('quantity', 1))
        cart_item.save()

        serializer = self.serializer_class(cart.cartitem_set.all(), many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        cart_item = get_object_or_404(Cart, id=id, cart__user=request.user)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)