from rest_framework import viewsets
from core.models import Service
from core.serializers import ServiceModelSerializer


class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer
