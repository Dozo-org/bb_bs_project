from common.serializers import TagSerializer
from rest_framework import serializers

from .models import Right


class RightSerializer(serializers.ModelSerializer):
    tags = TagSerializer()

    class Meta:
        model = Right
        fields = "__all__"
