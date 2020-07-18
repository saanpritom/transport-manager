from rest_framework import serializers
from .models import (VehicleTypeModel, VehicleManufacturerModel)


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTypeModel
        exclude = ['created_at', 'updated_at']


class VehicleManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleManufacturerModel
        exclude = ['created_at', 'updated_at']
