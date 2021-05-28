from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventList, EventParticipantList

router = DefaultRouter()
router.register(r'events', EventList, 'city_list')
router.register(r'event-participants', EventParticipantList, 'current_city')


urlpatterns = [
    path('', include(router.urls)),
]
