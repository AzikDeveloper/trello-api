from rest_framework.permissions import BasePermission


class IsAdminOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_staff) or request.method == 'POST'


class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_staff
