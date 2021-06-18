from django.contrib.admin import ModelAdmin, register

from .models import PlaceTag, Place


@register(PlaceTag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    ordering = ('name',)


@register(Place)
class PlaceAdmin(ModelAdmin):
    list_display = (
        'title', 'address', 'city','pubDate', 'description',
        'chosen', 'gender', 'age',
        'activity_type', 'link', 'imageUrl'
    )
    search_fields = ('title', 'city', 'tag')
    list_filter = ('chosen', 'activity_type', 'age')
    empty_value_display = '-пусто-'
    ordering = ('title',)
