from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_authenticated:
                return bool( 
                    request.user.is_admin is True
                    or request.user.is_superuser is True
                )


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            if request.user.is_authenticated:
                return bool( 
                    request.user.is_admin is True
                    or request.user.is_superuser is True
                )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(
            obj.owner and request.user.is_authenticated
            or request.user.is_admin is True
            or request.user.is_superuser is True
        )
