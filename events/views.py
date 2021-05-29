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
    http_method_names = ['get']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Event.objects.filter(city__in=self.request.user.city.all()).order_by('start_at')
        city_by_id = self.request.query_params.get('city')
        return Event.objects.filter(city=city_by_id).order_by('start_at')


class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer
    http_method_names = ['get', 'post', 'delete']
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

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.request.data.get('event'))
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        event = Event.objects.get(pk=instance.event.id)
        event.taken_seats -= 1
        event.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
