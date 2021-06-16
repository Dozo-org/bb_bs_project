from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import PlaceSerializer
from .models import Place, Tag
from common.models import Profile

class PlacesViewSet(viewsets.ModelViewSet):
    # TODO: filter by city, maybe default city?
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    http_method_names = ['get']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=self.request.user)
            return Place.objects.filter(city=profile.city)
        return Place.objects.all()