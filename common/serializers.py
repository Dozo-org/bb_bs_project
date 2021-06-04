from rest_framework import serializers

from .models import User, City


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


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = City
