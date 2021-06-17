from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import PlaceSerializer, TagSerializer
from .models import Place, Tag
from common.models import Profile


class CustomViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Pk lookup not allowed
    """
    pass


class PlacesViewSet(CustomViewSet):
    # TODO: filter by city, maybe default city?
    serializer_class = PlaceSerializer
    http_method_names = ['get']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=self.request.user)
            return Place.objects.filter(city=profile.city)
        return Place.objects.all()

    # TODO: add pagination for action
    @action(methods=['GET',], detail=False,
            url_path='tags', url_name='tags')
    def get_tags(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
