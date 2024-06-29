from django.db import models


class Post(models.Model):

    # id = PrimaryKey, implicit
    title = models.CharField(max_length=100, default="No Title")
    text = models.TextField()

    def __str__(self):
        return f"Post #{self.id}: {self.title}"

class Comment(models.Model):

    # id
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment #{self.id} for {self.post}"