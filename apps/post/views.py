from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from apps.post.models import Post, Category
from apps.post.serializers import CreatePostSerializer, CategorySerializer


class UserCreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer