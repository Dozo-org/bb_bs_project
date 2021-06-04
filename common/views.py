from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated)
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import City, User
from .permissions import (IsAdmin, IsSuperuser)
from .serializers import CitySerializer, UserSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all().order_by('-isPrimary')
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated, IsSuperuser | IsAdmin)
    lookup_field = 'name'


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsSuperuser | IsAdmin)

    def get_queryset(self):
        return User.objects.filter(
            username=self.request.user
        )

    action(detail=False, methods=['patch'])

    def partial_update(self, request):
        if (
                request.user.role != 'admin'
                and request.data.get('role') is not None
        ):
            return Response(
                {'role': 'Only Admin can change roles users'},
                status=HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(
            instance=request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    action(detail=False, methods=['put'])

    def update(self, request):
        if (
                request.user.role != 'admin'
                and request.data.get('role') is not None
        ):
            return Response(
                {'role': 'Only Admin can change roles users'},
                status=HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(
            instance=request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
