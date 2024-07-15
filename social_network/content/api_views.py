from rest_framework import permissions, viewsets

from content.models import Post
from content.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny,]