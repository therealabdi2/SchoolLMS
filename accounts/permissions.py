from rest_framework import permissions


class OwnerReadOnly(permissions.BasePermission):
    edit_methods = "GET"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False
