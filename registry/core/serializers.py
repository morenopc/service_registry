from rest_framework import serializers
from core.models import Service


class ServiceModelSerializer(serializers.ModelSerializer):

    """Service record data fields"""

    class Meta:
        model = Service
        exclude = ('id', )
