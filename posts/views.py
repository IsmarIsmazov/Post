from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
# from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    # filter_backends = (DjangoFilterBackend)
    queryset = Post.objects.all()


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
