from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('city', 'title', 'start_at', 'end_at', 'seats', 'taken_seats')
    search_fields = ('title', 'city', 'start_at', 'end_at')
    list_filter = ('title', 'city', 'start_at', 'end_at')
    ordering = ('city',)
    empty_value_display = '-пусто-'
    readonly_fields = ('taken_seats',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_moderator_reg:
            return queryset.filter(city=request.user.city)
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
