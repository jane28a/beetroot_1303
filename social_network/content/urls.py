from django.urls import path, include
from rest_framework import routers

from . import views
from . import api_views

router = routers.DefaultRouter()
router.register(r'posts', api_views.PostViewSet)

urlpatterns = [
    path("posts/", views.posts_list, name="posts_list"),
    path("posts/<int:post_id>/", views.post_details, name="post_details"),
    path("index/", views.index, name="posts_index"),
    path("api/posts/", views.api_posts, name="posts_api"),
    #path("api/", include(router.urls)),
]