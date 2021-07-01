import pytest
from model_bakery import baker

from places.models import Place
from common.models import Tag


class PlacesTags:
    endpoint = '/api/v1/places/tags/'

    @pytest.mark.django_db(transaction=True)
    def test_unauthorized_client(self, city, tags, client):
        response = client.get(self.endpoint)
        test_data = response.json()
        assert response.status_code != 404, (
            f'{self.endpoint} не существует'
        )
        assert response.status_code == 200, (
            f'{self.endpoint} для неавторизованного пользователя должен вернуть 200'
        )
        assert Tag.objects.count() == len(test_data), (
            f'{self.endpoint} для неавторизованного пользователя должен вернуть все объекты Tags'
        )