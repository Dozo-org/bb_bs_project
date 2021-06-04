from django.contrib.admin import ModelAdmin, register

from .models import User, City


@register(User)
class UserAdmin(ModelAdmin):

    list_display = ('username', 'role', 'email', 'city')
    empty_value_display = '-пусто-'


@register(City)
class CityAdmin(ModelAdmin):

    list_display = ('name', 'isPrimary')
    empty_value_display = '-пусто-'


