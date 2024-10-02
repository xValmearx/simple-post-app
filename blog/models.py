from django.db import models
from django.urls import reverse

# Create your models here.


# super user = caleb, password
class Post(models.Model):
    """Blog Post"""

    title = models.CharField(max_length=200)

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")

    body = models.TextField()

    create = models.DateTimeField(auto_now_add=True)

    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Get absolute url for this instance"""

        return reverse("post_details", kwargs={"pk": self.pk})
