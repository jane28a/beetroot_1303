from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("post/<int:post_id>/", views.post, name="post"),
]