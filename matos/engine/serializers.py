from rest_framework import serializers
from models import Operation


class OperationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    operation = serializers.CharField(required=True, max_length=30)
    numbers = serializers.JSONField(required=True)
    result = serializers.FloatField(required=False)
    ip = serializers.IPAddressField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Operation` instance, given the validated data.
        """
        return Operation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Operation` instance, given the validated data.
        """
        instance.operation = validated_data.get('operation', instance.operation)
        instance.save()
        return instance
