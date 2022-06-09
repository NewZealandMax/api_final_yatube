from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, serializers, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post
from .permissions import AccessPermission
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer


User = get_user_model()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AccessPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AccessPermission,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        queryset = user.follower.all()
        return queryset

    def perform_create(self, serializer):
        author = self.request.data['following']   # Не очень понимаю, зачем здесь тоже проверка, 
        if self.request.user.username == author:  # но иначе валидатор почему-то не работает
            raise serializers.ValidationError('Нельзя подписаться на самого себя!')
        serializer.save(user=self.request.user)
