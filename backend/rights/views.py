from rest_framework import generics

from .filters import RightFilter
from .models import Right, Tag_Right
from .serializers import RightSerializer, TagSerializer


class RightList(generics.ListAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    filterset_class = RightFilter


class RightView(generics.RetrieveAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    lookup_field = 'pk'


class TagList(generics.ListAPIView):
    queryset = Tag_Right.objects.all()
    serializer_class = TagSerializer
