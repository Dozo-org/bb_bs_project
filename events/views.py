from rest_framework import status, serializers
from rest_framework.response import Response
from .models import Event, EventParticipant
from cities.models import Profile
from .serializers import EventSerializer, EventParticipantSerializer
from rest_framework.decorators import permission_classes, action
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    allowed_methods = ['get', ]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Event.objects.filter(city__in=self.request.user.city.all()).order_by('start_at')
        city_by_id = self.request.query_params.get('city')
        return Event.objects.filter(city=city_by_id).order_by('start_at')


class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event_id = self.request.data.get('event')
        event = get_object_or_404(Event, id=event_id)
        if event.taken_seats < event.seats:
            event.taken_seats += 1
            event.save()
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError({'seats': 'Нет доступных мест для регистрации'})

    def destroy(self, request, *args, **kwargs):
        event = Event.objects.get(id=self.kwargs['event'])
        event.taken_seats -= 1
        event.save()
        participate = EventParticipant(user=self.request.user, event=event)
        participate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
