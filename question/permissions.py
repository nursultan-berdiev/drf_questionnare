from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        if request.user.is_authenticated and request.user.is_staff:
            return True
