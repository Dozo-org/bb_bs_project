from common.models import Tag
from django.contrib.admin import ModelAdmin, register
from django.contrib import admin

from .models import Question


@register(Question)
class PlaceAdmin(ModelAdmin):
    list_display = (
        'question', 'answer', 'pubDate', 'chosen', 'get_tags'
    )
    readonly_fields = [
        'pubDate',
        'chosen',
    ]
    search_fields = ('question', 'city', 'tags')
    list_filter = ('tags',)
    empty_value_display = '-пусто-'
    ordering = ('-pubDate',)

    @admin.display(description='Теги')
    def get_tags(self, obj):
        qs = obj.list_tags()
        if qs:
            return list(qs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'tags':
            kwargs['queryset'] = Tag.objects.filter(model='questions')
        return super().formfield_for_manytomany(db_field, request, **kwargs)