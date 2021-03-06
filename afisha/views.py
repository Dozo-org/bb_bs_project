from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework import status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import EventFilter
from .main_data import event
from .models import Event, EventParticipant
from .pagination import EventSetPagination
from .serializers import EventSerializer, EventParticipantSerializer
from common.models import Tag
from common.serializers import TagSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    http_method_names = ['get']
    pagination_class = EventSetPagination
    filterset_class = EventFilter

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Event.objects.filter(
                city=self.request.user.profile.city).order_by('startAt')
        city_by_id = self.request.query_params.get('city')
        return Event.objects.filter(city=city_by_id).order_by('startAt')

    @action(methods=['GET', ], detail=False,
            url_path='tags', url_name='tags')
    def get_tags(self, request):
        tags = Tag.objects.filter(model='event')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = EventSetPagination

    def get_queryset(self):
        user = self.request.user
        queryset = EventParticipant.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        event_id = self.request.data.get('event')
        event = get_object_or_404(Event, id=event_id)
        if event.takenSeats < event.seats:
            event.takenSeats += 1
            event.save()
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError(
                {'seats': '?????? ?????????????????? ???????? ?????? ??????????????????????'})

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(),
                                event=self.request.data.get('event'))
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        event = Event.objects.get(pk=instance.event.id)
        event.takenSeats -= 1
        event.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MainViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    http_method_names = ['get']

    def get_queryset(self):
        out = Event.objects.all().order_by('startAt').exists()
        if out:
            return Event.objects.all().order_by('-startAt')
        return Event.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        if serializer.data:
            event_data = {'event': serializer.data[0]}
        else:
            event_data = {'event': {}}

        response_data = {
            **event_data,
        }
        response_data.update(event)
        return Response(response_data)
