from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
        )

        def create(self, validated_data):
            user = super().create({
                'username': validated_data['username']
            })
            user.set_password(validated_data['password'])
            user.save()
            return user

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name='user_api',
        read_only=True
    )
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'body'
        )

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail_api',
        read_only=True
    )
    author = serializers.HyperlinkedRelatedField(
        view_name='user_api',
        read_only=True
    )
    class Meta:
        model = Comment
        fields = (
            'id',
            'body',
            'post',
            'author'
        )