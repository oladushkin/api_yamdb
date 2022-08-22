from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff is True:
            return True


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff is True and request.user.is_admin is True:
            return True
