from django.forms import ModelForm

from content.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = ["title", "text"]
        exclude = ["id"]