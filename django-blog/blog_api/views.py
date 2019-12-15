from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

from .serializers import(
    UserSerializer, User,
    PostSerializer, Post,
    CommentSerializer, Comment
)

from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q


class HomeAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
    def get_queryset(self):
        return Post.objects.all()
        
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class SearchAPIView(generics.ListAPIView):
    """
    use form field name as q
    """
    serializer_class = PostSerializer
    def get_queryset(self):
        query = self.request.GET.get('q')
        posts = Post.objects.filter(
            Q(title__icontains=query)|
            Q(body__icontains=query)
        )
        return posts


class UserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = ''
    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()

class AccountAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes =[IsAuthenticated, ]
    authentication_classes = (TokenAuthentication, )
    def get_object(self):
        return self.request.user

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ''
    authentication_classes = (TokenAuthentication, )

class PostListAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
    def get_queryset(self):
        # user = User.objects.get(pk=self.kwargs['pk'])
        return Post.objects.filter(
            author__id = self.kwargs['pk']
            # author = user
        )

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
    
    def get_queryset(self):
        return Post.objects.filter(
            # author__username = self.request.user.username
            id = self.kwargs['pk']
        )

class CommentListAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
    
    def get_queryset(self):
        return Comment.objects.filter(
            post__id = self.kwargs['pk']
        )
    def perform_create(self, serializer):
        serializer.save(
            author_id=self.request.user.id, 
            post_id=self.kwargs['pk'])

class CommentDetailAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
    def get_queryset(self):
        return Comment.objects.filter(
            id = self.kwargs['pk']
        )