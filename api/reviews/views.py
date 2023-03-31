from .models import Review
from rest_framework import generics, status
from .serializers import ReviewSerializer
from rest_framework.response import Response


class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()