from rest_framework import serializers

from .models import Event, EventParticipant


class EventSerializer(serializers.ModelSerializer):
    booked = serializers.SerializerMethodField('get_booked')

    def get_booked(self, obj):
        user = self.context['request'].user
        if user.is_anonymous():
            return False
        elif EventParticipant.objects.filter(user=user, event=obj).exists():
            return True
        return False

    class Meta:
        fields = '__all__'
        model = Event


class EventParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipant
        fields = ['id', 'event']
