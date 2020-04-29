from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import PostSerializer
# from todos.models import Todo


class PostViewSet(viewsets.ModelViewSet):
    # queryset = Todo.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.posts.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
