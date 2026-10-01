from django.test import TestCase, Client
from .models import User, Post
import json

# Create your tests here.

class PostTestCase(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user(username='Emma', email='emma@gmail.com', password='testing123')
        self.post_1 = Post.objects.create(author=self.user_1, content="My first post")


    def test_valid_edit(self):
        login_successful = self.client.login(username='Emma', password='testing123')
        self.assertTrue(login_successful)

        response = self.client.post(f'/edit_post/{self.post_1.id}',
                    data = json.dumps({'content': 'Edited post'}),
                    content_type='application/json'
                    )
        self.assertEqual(response.status_code, 200)

        edited_post = Post.objects.get(id=self.post_1.id)
        self.assertEqual(edited_post.content, "Edited post")


    def test_invalid_user_edit(self):
        user_2 = User.objects.create_user(username='favor', email='favor@gmail.com', password='favoring123')

        login_successful = self.client.login(username='favor', password='favoring123')
        self.assertTrue(login_successful)

        response = self.client.post(f'/edit_post/{self.post_1.id}',
                    data = json.dumps({'content': 'Edited post'}),
                    content_type='application/json'
                    )
        self.assertEqual(response.status_code, 403)


    def test_empty_edit(self):
        login_successful = self.client.login(username='Emma', password='testing123')
        self.assertTrue(login_successful)

        response = self.client.post(f'/edit_post/{self.post_1.id}',
                    data = json.dumps({'content': ''}),
                    content_type='application/json'
                    )
        self.assertEqual(response.status_code, 400)

        edited_post = Post.objects.get(id=self.post_1.id)
        self.assertEqual(edited_post.content, "My first post")

