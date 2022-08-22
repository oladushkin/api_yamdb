from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(
            request.user and request.user.is_admin
            or request.user and request.user.is_superuser
        )


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(
            request.user and request.user.is_active
            or request.user and request.user.is_admin
            or request.user and request.user.is_superuser
        )
    
    def has_object_permission(self, request, view, obj):
        