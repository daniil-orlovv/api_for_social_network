from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):

    # Определяет права на уровне запроса и пользователя
    def has_permission(self, request, view):
        return True

    # Определяет права на уровне объекта
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
