import pytest
from model_bakery import baker

from events.models import Event, EventParticipant


class TestEventParticipants:
    endpoint = '/api/v1/event-participants/'

    @pytest.mark.django_db(transaction=True)
    def test_list_unauthorized(self, client):
        response = client.get(self.endpoint)
        assert response.status_code != 404, (f'Адрес {self.endpoint} не существует')
        assert response.status_code == 401, (
            f'Запрос к {self.endpoint} без токена должен возвращать 401'
        )

    @pytest.mark.django_db(transaction=True)
    def test_list_authorized(
            self, moderator, admin, admin_client,
            event_participant, event_participant_another
    ):
        baker.make_recipe(
            'tests.fixtures.event_participant',
            user=moderator,
            event=event_participant.event
        )
        response = admin_client.get(self.endpoint)
        assert response.status_code == 200, (
            f'Запрос к {self.endpoint} с токеном должен возвращать 200'
        )
        test_data = response.json()
        test_event = test_data[0]
        registration_num = EventParticipant.objects.filter(user=admin).count()
        assert len(test_data) == registration_num, (
            f'{self.endpoint} должен возвращать все регистрации пользователя'
        )
        assert test_event.get('event') == event_participant.event.id
        assert 'id' in test_event, (
            f'id нет в списке полей сериализатора модели EventParticipant'
        )
        assert 'event' in test_event, (
            f'event нет в списке полей сериализатора модели EventParticipant'
        )
