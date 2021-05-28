from rest_framework import generics

from .models import City, Profile
from .serializers import CitySerializer, ProfileSerializer
from .permissions import IsUserOrReadOnly
from rest_framework import permissions, viewsets
from rest_framework.decorators import permission_classes, action


@action(detail=True, methods=['get'])
@permission_classes([permissions.IsAuthenticated])
class CityList(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer


@action(detail=True, methods=['get', 'put', 'patch'])
@permission_classes([permissions.IsAuthenticated, IsUserOrReadOnly])
class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
