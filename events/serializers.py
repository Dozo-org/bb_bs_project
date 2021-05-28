from rest_framework import serializers

from .models import Event, EventParticipant


class EventSerializer(serializers.ModelSerializer):
    booked = serializers.SerializerMethodField('get_booked')

    def get_booked(self, obj):
        if EventParticipant.objects.filter(user=self.context['request'].user, event=obj).exists():
            return True
        return False

    class Meta:
        fields = '__all__'
        model = Event


class EventParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipant
        fields = ['id', 'event']
