from rest_framework import status
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order
from apps.carts.models import Cart
from rest_framework.permissions import IsAuthenticated
from apps.common.custom_permissions import IsOwnerOrReadOnly, IsSuperUser
from rest_framework.decorators import action


class OrderViewset(viewsets.GenericViewSet, generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsSuperUser]

    def get_queryset(self):
        return self.queryset.objects.filter(user=self.request.user)

    @action(detail=False, methods=["post"], url_path="place-order")
    def place_order(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        order_serializer = self.get_serializer(data=request.data)
        if order_serializer.is_valid():
            response = order_serializer.save(user=request.user, total_price=cart.total_price())
            cart.cartitem_set.all().delete()
            return Response({"message": "order created"}, status=status.HTTP_201_CREATED)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["get"], url_path="get-orders")
    def get_orders(self, request, *args, **kwargs):
        instance = self.get_object()
        order_items: OrderItem = instance.items.all()
        serializer = self.get_serializer(instance)
        serializer.data["order"] = self.get_serializer(instance).data
        serializer.data["order_items"] = OrderItemSerializer(order_items, many=True).data
        return Response(serializer.data, status=status.HTTP_200_OK)