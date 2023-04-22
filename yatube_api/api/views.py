from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Post, Comment, Follow, Group
from api.serializers import (
    PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer)


class CRUDPost(viewsets.ModelViewSet):
    """
    Создаем, получаем, изменяем и удаляем пост.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CRUDComment(viewsets.ModelViewSet):
    """
    Создаем, получаем, изменяем и удаляем комментарий. Получаем список
    комментариев.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
