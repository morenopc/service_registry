from django.db.models.query import QuerySet
from django.db.models import Count
from rest_framework import viewsets
from core.models import Service
from core.serializers import ServiceModelSerializer, ServiceSearchModelSerializer


class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer


class ServiceSearchViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSearchModelSerializer

    def get_queryset(self):

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all(
                                ).values('service', 'version'
                                ).order_by('service', 'version'
                                ).annotate(count=Count('service'))

        queryset = queryset.filter(**self.request.query_params.dict())

        return queryset
