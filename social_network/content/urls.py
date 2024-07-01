from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.posts_list, name="posts_list"),
    path("posts/<int:post_id>/", views.post_details, name="post_details"),
]