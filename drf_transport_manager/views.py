from rest_framework import viewsets
from .serializers import VehicleTypeSerializer


# Create your views here.
class VehicleTypeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = VehicleTypeSerializer
    queryset = serializer_class.Meta.model.objects.all()
