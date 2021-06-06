from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault

from .models import User, City, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'city'
        )
        model = User
        extra_kwargs = {
            'username': {'required': True},
        }


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Profile


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = City
