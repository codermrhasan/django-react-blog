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

        # def create(self, validated_data):
        #     user = super().create({
        #         'username': validated_data['username']
        #     })
        #     user.set_password(validated_data['password'])
        #     user.save()
        #     return user

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'authors_id',
            'authors_username',
            'title',
            'body',
            'total_comments',
        )
        def create(self, validated_data):
            post = Post.objects.create(**validated_data)
            print(self.request.user)
            post.author = self.request.user
            
            post.save()
            return post

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