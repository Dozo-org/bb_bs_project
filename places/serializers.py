from rest_framework import serializers

from .models import Place, PlaceTag


class InfoField(serializers.Field):
    def to_representation(self, place):
        display = ''
        if place.gender:
            display += place.get_gender(place.gender) + ', '
        display += str(place.age) + ' лет.'
        display += place.get_activity_type(place.activity_type) + ' отдых'
        return display


class PlaceReadSerializer(serializers.ModelSerializer):
    info = InfoField(source='*')

    class Meta:
        model = Place
        fields = [
            'id',
            'info',
            'chosen',
            'title',
            'address',
            'description',
            'link',
            'imageUrl',
            'city'
        ]

    def get_gender(self, obj):
        return obj.get_gender_display()


class PlaceWriteSerializer(serializers.ModelSerializer):
    info = InfoField(source='*', read_only=True)
    imageUrl = serializers.ImageField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    chosen = serializers.SerializerMethodField('get_chosen')

    def get_chosen(self, obj):  # TODO: place in view, when updated/created
        user = self.context['request'].user
        return user.is_mentor

    class Meta:
        model = Place
        fields = [
            'id',
            'info',
            'chosen',
            'title',
            'address',
            'description',
            'link',
            'imageUrl',
            'city'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceTag
        fields = serializers.ALL_FIELDS
