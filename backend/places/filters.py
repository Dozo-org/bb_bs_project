import django_filters

from .models import Place


class PlacesFilter(django_filters.FilterSet):
    class Meta:
        model = Place
        fields = {
            'age': ['lte', 'gte'],
            'tags__slug': ['in']
        }
