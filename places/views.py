from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import PlaceSerializer
from .models import Place, Tag

class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    http_method_names = ['get']
