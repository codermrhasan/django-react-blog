from django.urls import path
from .views import ( 
    HomeAPIView, SearchAPIView,
    AccountAPIView, UserListAPIView, UserAPIView, RegisterAPIView,
    PostListAPIView, PostDetailAPIView,
    CommentListAPIView, CommentDetailAPIView
)
from rest_framework.authtoken import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('openapi', get_schema_view(
        title="Blog Project API",
        description="API for all things …",
        version="1.0.0"
        ), name='openapi-schema'
    ),
    path('api-docs/', TemplateView.as_view(
        template_name='blog_api/swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'
    ),
    path('', HomeAPIView.as_view(), name='home_api'),
    path('search/', SearchAPIView.as_view(), name='search_api'),
    path('register/', RegisterAPIView.as_view(), name='register_api'),
    path('login/', views.obtain_auth_token, name='login_api'),
    path('users/', UserListAPIView.as_view(), name='user_list_api'),
    path('users/<int:pk>/', UserAPIView.as_view(), name='user_api'),
    path('account/', AccountAPIView.as_view(), name='account_api'),
    path('users/<int:pk>/posts/', PostListAPIView.as_view(), name='post_list_api'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail_api'),
    path('posts/<int:pk>/comments/', CommentListAPIView.as_view(), name='comment_list_api'),
    path('posts/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail_api'),
]