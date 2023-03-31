from .models import Wishlist
from rest_framework import generics
from .serializers import WishlistSerializer


class WishlistListView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_queryset(self):
        user = self.request.user
        wishlists = Wishlist.objects.filter(user=user)
        return wishlists