from rest_framework import generics

from .filters import RightFilter
from .models import Right
from .pagination import RightsSetPagination
from .serializers import RightSerializer
from common.models import Tag
from common.serializers import TagSerializer


class RightList(generics.ListAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    filterset_class = RightFilter
    pagination_class = RightsSetPagination


class RightView(generics.RetrieveAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    lookup_field = 'pk'


class TagList(generics.ListAPIView):
    queryset = Tag.objects.filter(model='rights')
    serializer_class = TagSerializer
