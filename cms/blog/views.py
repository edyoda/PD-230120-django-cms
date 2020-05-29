from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

# def index(request):
#     return HttpResponse("Welcome to my blog!!!")

def index(request):
    posts = Post.objects.all()
    return render(request,"blog/stories.html",context = {"posts":posts})

# def index2(request):
#     return render(request,"temp.html")

def post_details(request,id):
    try:
        post = Post.objects.get(id = id)
        return render(request,"blog/blog-post.html",context = {"post":post})
    except:
        return HttpResponse("Welcome to my blog!!!")




# blog 
#     \static
#         \blog 
#             images 
#                a.jpeg 

# 127.0.0.1:8000/static/a.jpeg 
