from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username="testuser", email="test@email.com", password="secret")

        cls.post = Post.objects.create(title="A good title", body="Nice body content", author=cls.user)

    def test_user_model(self):
        """Test tge Post Model"""

        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exist_at_correct_location_listview(self):
        """Test URL exist at correct location for the listview"""
        repsonce = self.client.get("/")
        self.assertEqual(repsonce.status_code, 200)

    def test_url_exist_at_correct_location_detailview(self):
        """test URL exist at correct location for the detailview"""
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        responce = self.client.get(reverse("home"))
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, "Nice body content")
        self.assertTemplateUsed(responce, "home.html")

    def test_post_detailview(self):
        """Test Post detalview"""
        response = self.client.get(
            reverse("post_detail", kwargs={"pk": self.post.pk}),
        )
        no_response = self.client.get("/post/1000000/")
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")
