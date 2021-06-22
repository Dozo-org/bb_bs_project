from rest_framework import serializers

from .models import Right, Tag_Right


class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag_Right
        fields = serializers.ALL_FIELDS
