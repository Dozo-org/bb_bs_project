from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView

from .serializers import PlaceReadSerializer, PlaceWriteSerializer
from .models import Place
from common.models import Profile, Tag
from common.serializers import TagSerializer
from .filters import PlacesFilter
from .pagination import PlaceSetPagination


class CustomViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Pk lookup not allowed
    """
    pass


class PlacesListViewSet(CustomViewSet):
    serializer_class = PlaceReadSerializer
    filterset_class = PlacesFilter
    pagination_class = PlaceSetPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=self.request.user)
            return Place.objects.filter(city=profile.city, verified=True)
        city = self.request.query_params.get('city')
        return Place.objects.filter(verified=True,city__name=city)

    @action(methods=['GET', ], detail=False,
            url_path='tags', url_name='tags')
    def get_tags(self, request):
        tags = Tag.objects.filter(model='place')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class PlaceRetreiveUpdate(RetrieveUpdateAPIView, CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlaceReadSerializer
        return PlaceWriteSerializer

    def get_object(self):
        pid = self.request.query_params.get('place')
        if not pid:
            return None
        return get_object_or_404(Place, pk=pid)

    def perform_update(self, serializer):
        serializer.save(chosen=self.request.user.is_mentor)

    def perform_create(self, serializer):
        serializer.save(chosen=self.request.user.is_mentor)
