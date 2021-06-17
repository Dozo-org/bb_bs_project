from django.contrib.admin import ModelAdmin, register

from .models import Tag, Place


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    ordering = ('name',)


@register(Place)
class PlaceAdmin(ModelAdmin):
    list_display = (
        'title', 'address', 'city', 'description',
        'chosen', 'gender', 'age',
        'activity_type', 'link', 'imageUrl'
    )
    search_fields = ('title', 'city', 'tag')
    list_filter = ('chosen', 'activity_type', 'age')
    empty_value_display = '-пусто-'
    ordering = ('title',)
