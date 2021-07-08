from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView

from .serializers import QuestionGetSerializer, QuestionPostSerializer
from .models import Question
from .filters import QuestionFilter
from common.models import Profile, Tag
from common.serializers import TagSerializer


class ListCreateViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    pass


class ListCreateQuestionsViewSet(ListCreateViewSet):
    queryset = Question.objects.exclude(answer__exact='')
    permission_classes = [permissions.AllowAny]
    filterset_class = QuestionFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionGetSerializer
        return QuestionPostSerializer

    @action(methods=['GET', ], detail=False,
            url_path='tags', url_name='tags')
    def get_tags(self, request):
        tags = Tag.objects.filter(model='questions')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)