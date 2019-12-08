from django.test import TestCase
from project.factories import (
    UserFactory, PostFactory, CommentFactory
)

class TestPostModels(TestCase):
    def setUp(self):
        self.post = PostFactory(
            title = 'First Title',
            body = 'This is our first post. Welcome to first post.'
        )

    def test_default_post_attrs(self):
        self.assertEqual(self.post.title, 'First Title')
        self.assertEqual(self.post.body, 'This is our first post. Welcome to first post.')

class TestCommentModels(TestCase):
    def setUp(self):
        self.post = PostFactory(
            title = 'First Title',
            body = 'This is our first post. Welcome to first post.'
        )
        self.comment = CommentFactory(
            body = 'This is first comment.'
        )

    def test_default_budget_attrs(self):
        self.assertEqual(self.comment.body, 'This is first comment.')

