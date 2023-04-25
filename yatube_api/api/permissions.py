from rest_framework import permissions


class AuthAuthorOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            or view.action in ('retrieve', 'list')
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or view.action in ('retrieve', 'list')
        )
