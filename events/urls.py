from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, EventParticipantViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, 'city_list')
router.register(r'event-participants', EventParticipantViewSet, 'current_city')


urlpatterns = [
    path('', include(router.urls)),
]
