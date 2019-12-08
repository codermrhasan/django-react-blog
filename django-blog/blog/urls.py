from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    PostCreateView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentDeleteView
)

# cache_page(60*15)

urlpatterns = [
    path('create-post/', PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/posts/', (PostListView.as_view()), name='posts'),
    path('posts/<int:pk>/', (PostDetailView.as_view()), name='post_detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/create_comment/', CommentCreateView.as_view(), name='create_comment'),
    path('posts/<int:pk>/comment/<int:id>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]