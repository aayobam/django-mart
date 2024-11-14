
from apps.carts.models import Cart, CartItem
from apps.products.models import Product
from .serializers import CartSerializer
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    @action(detail=False, methods=["post"], url_path="add-to-cart")
    def add_to_cart(self, request, *args, **kwargs):
        instance = self.get_object()
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)
        product = Product.objects.get(id=product_id)
        cart_product, created = CartItem.objects.get_or_create(cart=instance, product=product)
        cart_product.quantity += int(quantity)
        cart_product.save()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"], url_path="get-cart")
    def get_cart(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="checkout")
    def checkout(self, request):
        session = request.session.session_key
        cart = session.get('cart', {})
        for product_id, item in cart.items():
            product = get_object_or_404(Product, id=product_id)
            if product.count < item['quantity']:
                return Response({'message': 'Not enough stock for product {}'.format(product.name)}, status=status.HTTP_400_BAD_REQUEST)
            product.count -= item['quantity']
            product.save()
        session['cart'] = {}
        session.save()
        self.clear_cart(request)
        return Response({'message': 'order places successfully.'}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["delete"], url_path="clear-cart")
    def clear_cart(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.products.all().delete()
        return Response({"message": "Cart cleared successfully."}, status=status.HTTP_200_OK)