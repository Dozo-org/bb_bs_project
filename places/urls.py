from rest_framework.routers import DefaultRouter

from .views import PlacesListViewSet

router = DefaultRouter()
router.register(r'places', PlacesListViewSet, basename='places')
