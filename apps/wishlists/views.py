from apps.common.custom_permissions import IsOwnerOrReadOnly
from .models import Wishlist
from rest_framework import viewsets
from .serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated


class WishlistViewset(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) 