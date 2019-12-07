import factory
from django.contrib.auth.models import User
from blog.models import Post, Comment

class UserFactory(factory.django.DjangoModelFactory):
    """
    Create test User
    """
    class Meta:
        model = User
    
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

class PostFactory(factory.django.DjangoModelFactory):
    """
    Create test Post
    """
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    body = factory.Faker('paragraphs')
    author = factory.SubFactory(UserFactory)

class CommentFactory(factory.django.DjangoModelFactory):
    """
    Create test Comment
    """
    class Meta:
        model = Comment

    body = factory.Faker('sentence')
    post = factory.SubFactory(PostFactory)
    author = factory.SubFactory(UserFactory)