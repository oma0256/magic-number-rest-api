from rest_framework import permissions


class HasPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.auth is not None:
            grant_type = request.auth.application.get_authorization_grant_type_display()
            if request.user is None and grant_type == 'Client credentials':
                request.user = request.auth.application.user
                return True
            else:
                return False