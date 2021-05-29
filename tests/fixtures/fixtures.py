from model_bakery.recipe import Recipe
from model_bakery import baker
from events.models import Event
import pytest


@pytest.fixture
def city():
    return baker.make_recipe('tests.fixtures.city')


@pytest.fixture
def another_city():
    return baker.make_recipe('tests.fixtures.city')


@pytest.fixture
def event():
    return baker.make_recipe('tests.fixtures.event')


@pytest.fixture
def events():
    return baker.make_recipe('tests.fixtures.event', _quantity=5)
