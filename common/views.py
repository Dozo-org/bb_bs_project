from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from .models import City, User, Profile
from .permissions import (IsSuperuser, IsUserOrReadOnly)
from .serializers import CitySerializer, ProfileSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all().order_by('-isPrimary', 'name')
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_field = 'name'


class ProfileViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsUserOrReadOnly | IsSuperuser)
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'patch']

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user.username)
        city = get_object_or_404(City, pk=request.data['city'])
        serializer = self.get_serializer(
            instance=request.user.profile,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, city=city)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user.username)
        city = get_object_or_404(City, pk=request.data['city'])
        serializer = self.get_serializer(
            instance=request.user.profile,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, city=city)
        return Response(serializer.data)
