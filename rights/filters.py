import django_filters

from .models import Right


class RightFilter(django_filters.FilterSet):
    class Meta:
        model = Right
        fields = {
            'tags__slug': ['in'],
        }
