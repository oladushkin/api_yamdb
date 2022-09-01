from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_authenticated:
                return request.user.is_admin


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or (obj.author == request.user
                    or (request.user.is_authenticated
                        and (request.user.is_superuser or request.user.is_admin or request.user.role == 'moderator'))
                    )
                )
