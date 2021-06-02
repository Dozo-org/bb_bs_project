from django.urls import path, include
from .views import UsersViewSet, CityListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cities', CityListViewSet, 'city_list')


urlpatterns = [
    #path(r'v1/cites/', CityViewSet.as_view({'get': 'list'})),
    path(r'', UsersViewSet.as_view({'get': 'list',
                                               'patch': 'partial_update',
                                               'put': 'update'})),
]