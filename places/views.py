from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import PlaceReadSerializer, TagSerializer, PlaceWriteSerializer
from .models import Place, Tag
from common.models import Profile


class CustomViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Pk lookup not allowed
    """
    pass


class PlacesListViewSet(CustomViewSet):
    serializer_class = PlaceReadSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=self.request.user)
            return Place.objects.filter(city=profile.city, verified=True)
        return Place.objects.all()

    # TODO: add pagination for action
    @action(methods=['GET', ], detail=False,
            url_path='tags', url_name='tags')
    def get_tags(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class PlaceRetreiveUpdate(RetrieveUpdateAPIView):
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