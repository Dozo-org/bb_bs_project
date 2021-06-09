from django.contrib.admin import ModelAdmin, register

from .models import User, City, Profile


@register(User)
class UserAdmin(ModelAdmin):

    list_display = ('username', 'role')
    empty_value_display = '-пусто-'


@register(City)
class CityAdmin(ModelAdmin):

    list_display = ('name', 'isPrimary')
    empty_value_display = '-пусто-'


@register(Profile)
class ProfileAdmin(ModelAdmin):

    list_display = ('user',)
    empty_value_display = '-пусто-'


