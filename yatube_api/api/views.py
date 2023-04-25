from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import AuthAuthorOnlyPermission
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Group, Post, User


class CRUDPost(viewsets.ModelViewSet):
    """
    Создаем, получаем, изменяем и удаляем пост.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthAuthorOnlyPermission,)
    pagination_class = LimitOffsetPagination

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

    serializer_class = CommentSerializer
    permission_classes = (AuthAuthorOnlyPermission,)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.filter(post_id=post_id)


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

    serializer_class = FollowSerializer
    http_method_names = ['get', 'post']
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user_id = self.request.user.pk
        return User.objects.get(pk=user_id).follower.all()
