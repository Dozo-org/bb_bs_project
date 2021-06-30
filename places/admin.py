from django.contrib.admin import ModelAdmin, register
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import PlaceTag, Place


@register(PlaceTag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    ordering = ('name',)


@register(Place)
class PlaceAdmin(ModelAdmin):
    list_display = (
        'title','showOnMain', 'chosen', 'verified','get_tags',
        'address', 'city', 'pubDate', 'description',
        'gender', 'age',
        'activity_type', 'link', 'imageUrl'
    )
    readonly_fields = [
        'pubDate',
    ]
    search_fields = ('title', 'city', 'tags')
    list_filter = ('chosen', 'showOnMain', 'activity_type', 'age','tags')
    empty_value_display = '-пусто-'
    ordering = ('chosen','-pubDate')

    @admin.display(description=_('Теги'))
    def get_tags(self, obj):
        qs = obj.list_tags()
        if qs:
            return list(qs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_moderator_reg or request.user.is_moderator:
            return queryset.filter(city=request.user.profile.city)
        return queryset

    def get_form(self, request, obj=None, **kwargs):
        form = super(PlaceAdmin, self).get_form(request, obj, **kwargs)
        if request.user.is_moderator_reg:
            form.base_fields['city'].initial = request.user.profile.city
            form.base_fields['city'].disabled = True
            form.base_fields['city'].help_text = 'Вы можете добавить рекомендацию только в своем городе'
        return form

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff
