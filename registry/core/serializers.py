from rest_framework import serializers
from core.models import Service


class ServiceModelSerializer(serializers.ModelSerializer):

    """Service record data fields"""

    class Meta:
        model = Service
        fields = '__all__'


class ServiceUpdateModelSerializer(serializers.ModelSerializer):

    """Service update data fields"""

    class Meta:
        model = Service
        fields = ('change', )

    def update(self, instance, validated_data):

        instance.change = 'changed'
        instance.save()

        return instance


class ServiceDestroyModelSerializer(serializers.ModelSerializer):

    """Service remove data fields"""

    class Meta:
        model = Service
        fields = ('service', 'change')


class ServiceSearchModelSerializer(serializers.ModelSerializer):

    """Service search data fields"""

    def __init__(self, *args, **kwargs):

        # Instantiate the superclass normally
        super(ServiceSearchModelSerializer, self).__init__(*args, **kwargs)

        service = self.context['request'].query_params.get('service', None)
        version = self.context['request'].query_params.get('version', None)

        # remove version from fields
        if version is None:
            self.fields.pop('version')

    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Service
        fields = ('service', 'version', 'count')
