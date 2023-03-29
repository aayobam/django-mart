from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order
from apps.carts.models import Cart
from rest_framework.permissions import IsAuthenticated
from apps.common.custom_permissions import IsOwnerOrReadOnly, IsSuperUser


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(user=self.request.user, total_price=cart.total_price())

    def post(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        order_serializer = self.serializer_class(data=request.data)
        if order_serializer.is_valid():
            # Create the order
            response = order_serializer.save(user=request.user, total_price=cart.total_price())
            
            # Clear the cart
            cart.cartitem_set.all().delete()
            
            # Return response
            return Response({'message':'order created'}, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer()
    permission_classes = [IsOwnerOrReadOnly, IsSuperUser]