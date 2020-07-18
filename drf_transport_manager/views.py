from rest_framework import viewsets
from .serializers import (VehicleTypeSerializer, VehicleManufacturerSerializer)


# Create your views here.
class VehicleTypeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = VehicleTypeSerializer
    queryset = serializer_class.Meta.model.objects.all()


class VehicleManufacturerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = VehicleManufacturerSerializer
    queryset = serializer_class.Meta.model.objects.all()
