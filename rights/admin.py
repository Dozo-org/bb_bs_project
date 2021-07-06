from django.contrib.admin import ModelAdmin, register

from .models import Right
from common.models import Tag


@register(Right)
class RightAdmin(ModelAdmin):
    search_fields = ('title', 'description', 'text')
    list_filter = ('title', 'tags')
    empty_value_display = '-пусто-'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'tags':
            kwargs['queryset'] = Tag.objects.filter(model='rights')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff
