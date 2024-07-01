from django.http import (
    HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from content.forms import PostForm
from content.models import Post

def posts_list(request):
    if request.method == "GET":
        # return HttpResponse(Post.objects.all())
        context = {"posts": Post.objects.all(), "form": PostForm()}
        return render(request, "content/posts.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return HttpResponseRedirect(reverse("post_details", args=[new_post.id]))
        else:
            return HttpResponseBadRequest({"details": form.errors})
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "content/post_details.html", {"post": post})