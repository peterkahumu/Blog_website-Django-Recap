from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

import uuid
from .models import Post


# Create your tests here.
class PostTest(TestCase):
    """Class to test the posts model."""

    @classmethod
    def setUpTestData(cls):
        """Create test data."""
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@test.com", password="test123"
        )

        cls.post = Post.objects.create(
            title="Test Post", author=cls.user, body="This is a test Post."
        )
        cls.post2 = Post.objects.create(
            title="Test Post 2", author=cls.user, body="This is the second test data."
        )

    def setUp(self):
        """Prepare test clients for home and post endpoints."""
        self.home_url = self.client.get("/")
        self.home_name = self.client.get(reverse("home"))

        self.post_url = self.client.get(self.post.get_absolute_url())
        self.post_invalid = self.client.get(
            reverse("post-detail", kwargs={"pk": uuid.uuid4()})
        )

    def test_urls(self):
        """Test the URLs to ensure they return the expected status code"""
        self.assertEqual(self.home_name.status_code, 200)
        self.assertEqual(self.home_url.status_code, 200)
        self.assertEqual(self.post_url.status_code, 200)
        self.assertEqual(self.post_invalid.status_code, 404)

        # test the absolute url
        self.assertEqual(self.post.get_absolute_url(), f'/blog/{self.post.id}/')

    def test_templates(self):
        """Test templates to ensure expected behaviour."""
        # templates used
        self.assertTemplateUsed(self.home_url, "posts/home.html")
        self.assertTemplateUsed(self.post_url, "posts/post_detail.html")

        # template content.
        self.assertContains(self.home_url, "Test Post")
        self.assertContains(self.home_name, "This is the second test data.")
        self.assertContains(self.post_url, "This is a test Post.")
    
    def test_post_model(self):
        """Test model to ensure it is working as expected."""
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.body, "This is a test Post.")
        self.assertEqual(str(self.post), "Test Post")
    
    def test_home_queryset(self):
        """Test the queryset has a predefined number of response items."""
        response = Post.objects.all()
        self.assertEqual(response.count(), 2) # exactly two objects.
    
    def test_context_data(self):
        """Test that the context is as expected."""
        self.assertIn('posts', self.home_name.context)
        self.assertIn('post', self.post_url.context)