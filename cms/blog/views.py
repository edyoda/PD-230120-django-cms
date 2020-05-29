from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def index(request):
    return HttpResponse("Welcome to my blog!!!")

def post_details(request,id):
    try:
        post = Post.objects.get(id = id)
        return HttpResponse("Welcome to my blog!!! {}".format(post.title))
    except:
        return HttpResponse("Welcome to my blog!!!")
