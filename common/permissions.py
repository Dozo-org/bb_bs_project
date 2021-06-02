from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Editing an object is only possible for the Moderator."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_moderator


class IsModeratorReg(permissions.BasePermission):
    """Editing an object is only possible for the Region Moderator."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator_reg

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_moderator_reg


class IsMentor(permissions.BasePermission):
    """Editing an object is only possible for the Mentor"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_mentor

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_mentor


class IsAdmin(permissions.BasePermission):
    """Editing an object is only possible for the Admin."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    """Readable by all.

    The object can only be edited by the Administrator.
    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated and request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated and request.user.is_admin)


class IsSuperuser(permissions.BasePermission):
    """Editing an object is only possible for the Superuser."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_superuser


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, profile):
        if request.method in permissions.SAFE_METHODS:
            return True
        return profile.user == request.user
