from rest_framework import serializers

from common.serializers import TagSerializer
from .models import Question


class QuestionGetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'tags',
            'question',
            'answer',
            'pubDate',
            'chosen'
        ]


class QuestionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question']
