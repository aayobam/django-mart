from rest_framework import viewsets
from .models import Logistic


class LogisticSerializer(viewsets.ModelViewSet):
    queryset = Logistic.objects.all()
    permission_classes = []