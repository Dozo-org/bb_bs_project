from model_bakery.recipe import Recipe, seq, foreign_key
from django.contrib.auth import get_user_model

from afisha.models import Event, EventParticipant
from common.models import City
from places.models import Place, Tag

User = get_user_model()

city = Recipe(
    City,
    name=seq('City')
)

admin = Recipe(
    User,
    username=seq('user'),
    password=seq('PassWord'),
    email=seq('admin', suffix='@gmail.com'),
    role='admin',
)

moderator = Recipe(
    User,
    username=seq('moderator'),
    password=seq('PassWord'),
    email=seq('moderator', suffix='@gmail.com'),
    role='moderator'
)

event = Recipe(
    Event,
    title=seq('ул Тест'),
    city=foreign_key(city),
    seats=2,
)

event_participant = Recipe(
    EventParticipant,
    user=foreign_key(admin),
    event=foreign_key(event)
)

tag = Recipe(
    Tag,
    name=seq('Tag_name'),
    slug=seq('tag-')
)