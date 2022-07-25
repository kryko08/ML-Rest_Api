from pkg_resources import safe_name
from rest_framework import permissions


class IsRequestOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        safe_methods = ["GET", 'HEAD', 'OPTIONS']
        if request.method not in safe_methods:
            return request.user.id == obj.user.id or request.user.is_superuser
        return True
        