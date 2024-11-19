from rest_framework import viewsets
from .serializers import DriverSerializer
from .models import Driver


class DriverViewset(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = []
