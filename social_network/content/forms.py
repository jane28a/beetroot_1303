from django.forms import ModelForm

from content.models import Post
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = ["title", "text"]
        exclude = ["id"]

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]