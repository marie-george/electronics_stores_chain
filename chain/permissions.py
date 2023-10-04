from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """Доступ предоставляется только активным пользователям"""
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False
