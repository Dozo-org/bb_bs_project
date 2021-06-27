from rest_framework.routers import DefaultRouter

from .views import CityViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet, 'city_list')
router.register(r'profile', ProfileViewSet, 'profile')
