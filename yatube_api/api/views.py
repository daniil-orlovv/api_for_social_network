from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Comment, Follow, Group
from api.serializers import (
    PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer)
from api.permissions import AuthAuthorOnlyPermission

class CRUDPost(viewsets.ModelViewSet):
    """
    Создаем, получаем, изменяем и удаляем пост.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthAuthorOnlyPermission,)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('text',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return (permissions.IsAuthenticatedOrReadOnly(),)
        return super().get_permissions()


class CRUDComment(viewsets.ModelViewSet):
    """
    Создаем, получаем, изменяем и удаляем комментарий. Получаем список
    комментариев.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthAuthorOnlyPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('text',)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return (permissions.IsAuthenticatedOrReadOnly(),)
        return super().get_permissions()

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        comments = Comment.objects.filter(post_id=post_id)
        return comments


class ListRetrieveGroup(viewsets.ReadOnlyModelViewSet):
    """
    Получаем список групп или информацию о группе.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RetrieveCreateFollow(viewsets.ModelViewSet):
    """
    Получаем или создаем подписку.
    """

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("user__username", "following__username",)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user_id = self.request.user.pk
        follows = Follow.objects.filter(user_id=user_id)
        return follows
