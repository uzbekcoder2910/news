from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Post Title', content='Post Content')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_content = f'{post.content}'
        self.assertEqual(expected_object_title, 'Post Title')
        self.assertEqual(expected_object_content, 'Post Content')


class PostListViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Post Title 2', content='Post Content 2')

    def test_views_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_views_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_views_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')