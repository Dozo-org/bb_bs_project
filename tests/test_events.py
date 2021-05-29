import pytest
from model_bakery import baker

from events.models import Event


class TestEventsList:
    endpoint = '/api/v1/events/'

    @pytest.mark.django_db(transaction=True)
    def test_unauthorized_client(self, city, another_city, client):
        baker.make_recipe(
            'tests.fixtures.event',
            _quantity=5,
            city=city
        )
        baker.make_recipe(
            'tests.fixtures.event',
            _quantity=3,
            city=another_city
        )
        response = client.get(self.endpoint)
        test_data = response.json()
        assert response.status_code != 404, (
            f'Адрес {self.endpoint} не доступен'
        )
        assert response.status_code == 200, (
            f'Адрес {self.endpoint} для неавторизованного пользователя должен вернуть 200'
        )
        assert len(test_data) == 0, (
            f'Запрос к {self.endpoint} без GET параметра не должен возвращать объекты'
        )
        response = client.get(self.endpoint + f'?city={city.id}')
        test_data = response.json()
        assert response.status_code == 200, (
            f'Запрос к {self.endpoint} с GET параметром city должен вернуть 200'
        )
        assert len(test_data) == 5, (
            f'Запрос к {self.endpoint} GET параметром city должен вернуть только мероприятия в городе {city}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_authorized_client(self, city, admin, admin_client, moderator_client):
        admin_city = admin.city.all()[0]
        baker.make_recipe(
            'tests.fixtures.event',
            _quantity=5,
            city=admin_city
        )
        baker.make_recipe(
            'tests.fixtures.event',
            _quantity=3,
            city=city
        )
        response = admin_client.get(self.endpoint)
        test_data = response.json()
        assert response.status_code != 404, (
            f'Адрес {self.endpoint} для запроса с токеном недоступен'
        )
        assert response.status_code == 200, (
            f'Запрос к {self.endpoint} с токеном авторизации должен возвращать 200'
        )
        assert len(test_data) == Event.objects.filter(city=admin_city).count(), (
            f'Запрос к {self.endpoint} с токеном авторизации должен возвращать все события в городе пользователя'
        )
        response = moderator_client.get(self.endpoint)
        test_data = response.json()
        assert response.status_code == 200, (
            f'Адрес {self.endpoint} доступен для авторизованного пользователя с пустым полем города'
        )
        assert len(test_data) == 0, (
            f'Запрос к {self.endpoint} от пользователя с пустым полем города возвращает пустой ответ'
        )
