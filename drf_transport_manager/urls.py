from rest_framework.routers import DefaultRouter
from .views import VehicleTypeViewSet

router = DefaultRouter()
router.register(r'vehicle/types', VehicleTypeViewSet, basename='vehicles')
urlpatterns = router.urls
