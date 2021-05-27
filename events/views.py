from rest_framework import status
from rest_framework.response import Response
from .models import Event, EventParticipant
from .serializers import EventSerializer, EventParticipantSerializer
from rest_framework.decorators import permission_classes, action
from rest_framework import permissions, viewsets


@action(detail=True, methods=['get'])
class EventList(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Event.objects.filter(city=self.request.user.city).order_by('start_at')
        return Event.objects.filter(city__id=self.kwagrs['event']).order_by('start_at')

    serializer_class = EventSerializer


@action(detail=True, methods=['get', 'post', 'delete'])
@permission_classes([permissions.IsAuthenticated])
class EventParticipantList(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer

    def perform_create(self, serializer):
        event = Event.object.get(id=self.kwargs['event'])
        event.taken_seats += 1
        event.save()
        return serializer.save()

    def destroy(self, request, *args, **kwargs):
        event = Event.object.get(id=self.kwargs['event'])
        event.taken_seats -= 1
        event.save()
        participate = EventParticipant(user=self.request.user, event=event)
        participate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
