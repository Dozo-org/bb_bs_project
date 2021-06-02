from rest_framework import serializers

from .models import User, City, Profile


class UserSerializer(serializers.ModelSerializer):
    """User serialiser."""

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


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True)

    class Meta:
        fields = '__all__'
        model = Profile