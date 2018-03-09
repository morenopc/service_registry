from django.db.models import Count
from rest_framework import viewsets, mixins, generics, permissions
from rest_framework.exceptions import NotFound, APIException
from core.models import Service
from core.serializers import (
    ServiceModelSerializer, ServiceSearchModelSerializer,
    ServiceUpdateModelSerializer)


class ServiceSearchNotFound(NotFound):

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail

        if code is None:
            code = self.default_code

        self.detail = detail


class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer


class ServiceSearchGenericViewSet(mixins.RetrieveModelMixin,
                                  viewsets.GenericViewSet):

    queryset = Service.objects.all(
                                ).values('service', 'version'
                                ).order_by('service', 'version'
                                ).annotate(count=Count('service'))
    serializer_class = ServiceSearchModelSerializer

    def get_object(self):

        """Get search result"""

        service = self.request.query_params.get('service', None)
        version = self.request.query_params.get('version', None)

        # parameters validation
        if service is None and version is None:
            raise APIException('Search parameters (service or version) '
                                'could not be found')

        elif service is None:
            raise APIException('Search parameter (service) '
                                'could not be found')

        # Finding service with or without version
        try:
            return self.queryset.get(**self.request.query_params.dict())

        except Service.DoesNotExist as e:
            # Finding non existing service
            details_dict = self.request.query_params.dict()
            details_dict.update({'count': 0})
            raise ServiceSearchNotFound(details_dict)

        except Exception as e:
            raise APIException(e)


class ServiceUpdateAPIView(generics.UpdateAPIView):
    """Update service"""
    queryset = Service.objects.all()
    serializer_class = ServiceUpdateModelSerializer
