from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the social network index.")

def post(request, post_id):
    return HttpResponse(f"You're looking at post {post_id}")

def hello_user(request, username):
    return HttpResponse(f"Hello, {username.capitalize()}!")
