from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
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


admin.site.register(Event, EventAdmin)
