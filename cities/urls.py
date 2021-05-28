from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CityList, ProfileView

router = DefaultRouter()
router.register(r'cities', CityList, 'city_list')
router.register(r'profile', ProfileView, 'current_city')


urlpatterns = [
    path('', include(router.urls)),
]
