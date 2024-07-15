from datetime import date
from django.http import (
    HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed,
    JsonResponse
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from content.forms import PostForm, SignUpForm
from content.models import Post

def signup(request):
    if request.method == "GET":
        return render(request, "content/signup.html", {"form": SignUpForm()})
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            ... # save new user instance with User.objects.create_user()
            # redirect to login page
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

def api_posts(request):
    result = list()
    for post in Post.objects.all():
        result.append({
            "id": post.id,
            "title": post.title,
            "text": post.text
        })
    return JsonResponse(result, safe=False)

@login_required
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

@login_required
def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "content/post_details.html", {"post": post})

def index(request):
    context = {
        "today": date.today().strftime("%Y-%m-%d"),
        "number": 19,
        "the_list": [1, 2, 3, 4, 5, 6, 8]
    }
    return render(request, "content/index.html", context)