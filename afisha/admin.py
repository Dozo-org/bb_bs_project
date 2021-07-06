from common.models import Tag
from django.contrib.admin import ModelAdmin, register, site

from afisha.models import Event, EventParticipant


@register(Event)
class EventAdmin(ModelAdmin):
    list_display = ('city', 'title', 'startAt', 'endAt', 'seats',
                    'takenSeats')
    search_fields = ('title', 'city', 'startAt', 'endAt')
    list_filter = ('title', 'city', 'startAt', 'endAt')
    ordering = ('city',)
    empty_value_display = '-пусто-'
    readonly_fields = ('takenSeats',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_moderator_reg:
            return queryset.filter(city=request.user.profile.city)
        return queryset

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'tags':
            kwargs['queryset'] = Tag.objects.filter(model='event')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def has_module_permission(self, request):
        return not request.user.is_anonymous

    def has_view_permission(self, request, obj=None):
        return not request.user.is_anonymous

    def has_add_permission(self, request):
        return not request.user.is_anonymous

    def has_change_permission(self, request, obj=None):
        return not request.user.is_anonymous

    def has_delete_permission(self, request, obj=None):
        return not request.user.is_anonymous

    def get_form(self, request, obj=None, **kwargs):
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        if request.user.is_moderator_reg:
            form.base_fields['city'].initial = request.user.profile.city
            form.base_fields['city'].disabled = True
            form.base_fields['city'].help_text = 'Вы можете добавить событие только в своем городе'
        return form


site.register(EventParticipant)
