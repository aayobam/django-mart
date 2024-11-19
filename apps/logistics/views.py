from rest_framework import viewsets
from .models import Logistic
from .serializers import LogisticSerializer


class LogisticViewSet(viewsets.ModelViewSet):
    queryset = Logistic.objects.all()
    serializer_class = LogisticSerializer
    permission_classes = []