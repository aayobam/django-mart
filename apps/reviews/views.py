from .models import Review
from rest_framework import viewsets
from .serializers import ReviewSerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = []

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
