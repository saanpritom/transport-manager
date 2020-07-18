from rest_framework import serializers
from .models import VehicleTypeModel


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTypeModel
        exclude = ['created_at', 'updated_at']
