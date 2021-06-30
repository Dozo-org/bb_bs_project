from django.contrib.admin import ModelAdmin, TabularInline, register, site
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import City, Profile


User = get_user_model()


class ProfileInline(TabularInline):
    model = Profile
    extra = 1


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    inlines = [
        ProfileInline,
    ]
    list_display = ('email', 'username', 'first_name', 'last_name', 'role')
    readonly_fields = ('last_login', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'role', 'is_staff', 'is_active')}),
        ('Personal info', {'classes': ('wide',), 'fields': ('email',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'username', 'role',
         'password1', 'password2')}),
    )

    def has_add_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)

    def has_module_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)


@register(City)
class CityAdmin(ModelAdmin):

    list_display = ('name', 'isPrimary')
    empty_value_display = '-пусто-'

    def has_add_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)

    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff


@register(Profile)
class ProfileAdmin(ModelAdmin):

    def has_add_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)

    def has_module_permission(self, request):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or (request.user.is_staff
                                             and request.user.is_admin)


site.unregister(Group)
site.register(User, CustomUserAdmin)
