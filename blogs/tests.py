from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

import uuid
from .models import Post


class TestPostModel(TestCase):
    """Tests for the Post model and its basic CRUD views."""

    @classmethod
    def setUpTestData(cls):
        """Create test data once for the whole TestCase."""
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
        """Prepare client GET responses used across tests."""
        self.home_url = self.client.get("/") # literal url used intetionally here.
        self.home_name = self.client.get(reverse("home"))

        self.post_url = self.client.get(self.post.get_absolute_url())
        self.post_invalid = self.client.get(
            reverse("post-detail", kwargs={"pk": uuid.uuid4()})
        )

    def test_urls_status_codes(self):
        """URLs return expected status codes."""
        self.assertEqual(self.home_name.status_code, 200)
        self.assertEqual(self.home_url.status_code, 200)
        self.assertEqual(self.post_url.status_code, 200)
        self.assertEqual(self.post_invalid.status_code, 404)

        # absolute url format
        self.assertEqual(self.post.get_absolute_url(), f"/post/{self.post.id}/")

    def test_templates_and_content(self):
        """Templates used and page content are correct."""
        self.assertTemplateUsed(self.home_url, "posts/home.html")
        self.assertTemplateUsed(self.post_url, "posts/post_detail.html")

        self.assertContains(self.home_url, "Test Post")
        self.assertContains(self.home_name, "This is the second test data.")
        self.assertContains(self.post_url, "This is a test Post.")

    def test_post_model_fields(self):
        """Model fields and __str__ behave as expected."""
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.body, "This is a test Post.")
        self.assertEqual(str(self.post), "Test Post")

    def test_home_queryset_count(self):
        """Ensure the initial queryset has exactly two posts."""
        self.assertEqual(Post.objects.count(), 2)

    def test_context_data(self):
        """Context from views contains expected keys."""
        self.assertIn("posts", self.home_name.context)
        self.assertIn("post", self.post_url.context)

    def test_post_createview(self):
        """Create view should create a new Post and redirect."""
        response = self.client.post(
            reverse("new-post"),
            {
                "title": "New Post",
                "author": self.user.id,
                "body": "New body",
            },
        )

        self.assertEqual(response.status_code, 302)

        created = Post.objects.first() # ordering should be handled at DB level.
        self.assertIsNotNone(created)
        self.assertEqual(created.title, "New Post")
        self.assertEqual(created.body, "New body")

    def test_post_updateview(self):
        """Update view should update the post and redirect."""
        response = self.client.post(
            self.post.get_update_url(),
            {"title": "New title", "body": "New Body"},
        )

        # UpdateView redirects on success
        self.assertEqual(response.status_code, 302)

        # Verify DB change
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "New title")
        self.assertEqual(self.post.body, "New Body")

    def test_post_update_non_existent_post(self):
        """Updating a non-existent post should return 404."""
        response = self.client.post(
            reverse("update-post", kwargs={"pk": uuid.uuid4()}),
            {"title": "Test Non-Existent", "body": "Test Non-existent."},
        )
        self.assertEqual(response.status_code, 404)

    def test_post_deleteview(self):
        """Delete view should remove the post and redirect."""
        response = self.client.post(
            reverse("delete-post", kwargs={"pk": self.post2.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)

    def test_delete_non_existent_post(self):
        """Deleting a non-existent post returns 404."""
        response = self.client.post(
            reverse("delete-post", kwargs={"pk": uuid.uuid4()})
        )
        self.assertEqual(response.status_code, 404)
