from django.urls import include, path
from .routers import CustomRouter
from .views import EventViewSet, EventParticipantViewSet

router = CustomRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'event-participants', EventParticipantViewSet, basename='event-participant')


urlpatterns = [
    path('', include(router.urls)),
]
