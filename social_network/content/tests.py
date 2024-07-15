from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from content.models import Post

class PostTests(TestCase):
    
    def test_of_test(self):
        self.assertTrue(True)

    def test_post_title(self):
        post = Post(text="Test post")
        post.save()
        self.assertEqual(post.title, "No Title")

    def test_post_list_api(self):
        client = Client()
        response = client.get("/content/api/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

    def test_post_create_api(self):
        client = Client()
        response = client.post("/content/api/posts/", 
            {"title": "New Post", "text": "New API Post"}
        )
        self.assertEqual(response.status_code, 201)

    def test_post_details(self):
        post = Post.objects.create(title="Test title", text="Test text")
        client = Client()
        response = client.get(f"/content/api/posts/{post.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Test title")
    
    def test_update_details(self):
        post = Post.objects.create(title="Test title", text="Test text")
        client = APIClient()
        response = client.put(f"/content/api/posts/{post.id}/",
            format="json",
            data = {"title": "Title Updated", "text": "Text Updated"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Title Updated")

    def test_posts_ui(self):
        user = User.objects.create_user(username="test", password="test")
        client = Client()
        result = client.login(username="test", password="test")
        self.assertEqual(result, True)
        response = client.get("/content/posts/")
        self.assertEqual(response.status_code, 200)
