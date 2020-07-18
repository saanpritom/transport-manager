from rest_framework.routers import DefaultRouter
from .views import VehicleTypeViewSet, VehicleManufacturerViewSet

router = DefaultRouter()
router.register(r'vehicle/types', VehicleTypeViewSet, basename='vehicle_types')
router.register(r'vehicle/manufactures', VehicleManufacturerViewSet, basename='vehicle_manufacturers')
urlpatterns = router.urls
