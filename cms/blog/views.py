from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category
from blog.forms import ContactUsForm,RegisterForm,PostForm
from django.views import View
from django.views import generic
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# def index(request):
#     return HttpResponse("Welcome to my blog!!!")

def index(request):
    posts = Post.objects.all()
    return render(request,"blog/stories.html",context = {"posts":posts})

class HomeView(View):

    def get(self,request):
        posts = Post.objects.all()
        return render(request,"blog/stories.html",context = {"posts":posts})


class PostListView(generic.ListView):
    model = Post 
    queryset = Post.objects.filter(status = "P")
    context_object_name = 'posts'
    template_name = "blog/stories.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

# def index2(request):
#     return render(request,"temp.html")

def post_details(request,id):
    try:
        post = Post.objects.get(id = id)
        return render(request,"blog/blog-post.html",context = {"post":post})
    except:
        return HttpResponse("Welcome to my blog!!!")

class PostView(View):
    def get(self,request,id):
        try:
            post = Post.objects.get(id = id)
            return render(request,"blog/blog-post.html",context = {"post":post})
        except:
            return HttpResponse("Welcome to my blog!!!")
        
class PostDetailView(LoginRequiredMixin,generic.DetailView):
    model = Post
    queryset = Post.objects.filter(status = "P")
    template_name = "blog/blog-post.html"
    login_url = reverse_lazy('login')
    # pk_url_kwarg = "id"

def contact_us_form_view(request):
    # print(request.method)
    # print(request.GET)
    if request.method == "GET":
        form = ContactUsForm()
        return render(request,"blog/contact-us.html",context = {"form":form})
    else:

        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Thank you for submitting the response")
        else:
            print(form.errors)
            return render(request,"blog/contact-us.html",context = {"form":form})
        


def register_form_view(request):
    # print(request.method)
    # print(request.GET)
    if request.method == "GET":
        form = RegisterForm()
        return render(request,"blog/register.html",context = {"form":form})
    else:

        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Thank you for submitting the response")
        else:
            print(form.errors)
            return render(request,"blog/register.html",context = {"form":form})

def post_form_view(request):
    # print(request.method)
    # print(request.GET)
    print(request.FILES)
    if request.method == "GET":
        form = PostForm()
        return render(request,"blog/post.html",context = {"form":form})
    else:

        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for submitting the response")
        else:
            print(form.errors)
            return render(request,"blog/post.html",context = {"form":form})

# class PostCreateView(View):
#     def get(self,request):
#         form = PostForm()
#         return render(request,"blog/post.html",context = {"form":form})

#     def post(self,request):
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank you for submitting the response")
#         else:
#             print(form.errors)
#             return render(request,"blog/post.html",context = {"form":form})



class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title','content','status','category','image','author']
    # form_class = PostForm
    template_name = "blog/post.html"
    # success_url = reverse_lazy("post-detail")

    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,                
            })
            # data = kwargs.get('data').dict()
            
            # data['author_id'] = self.request.user.profile.id
            # print(data)
            kwargs['initial']['author'] = self.request.user.profile
        print(kwargs)
        return kwargs

        


class AboutUs(generic.TemplateView):
    template_name = "404.html"

# class RedirectPost(generic.RedirectView):
#     url = reverse_lazy('home')





def post_update_form_view(request,id):
    # print(request.method)
    # print(request.GET)
    post = Post.objects.get(id = id)
    
    if request.method == "GET":
        form = PostForm(instance = post)
        return render(request,"blog/post.html",context = {"form":form})
    else:

        form = PostForm(request.POST,request.FILES,instance = post)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for submitting the response")
        else:
            print(form.errors)
            return render(request,"blog/post.html",context = {"form":form})


# blog 
#     \static
#         \blog 
#             images 
#                a.jpeg 

# 127.0.0.1:8000/static/a.jpeg 


# Post.objects.create(title = "",content = "")



# def prinval(val1,val2,val3):



# d = {"val1":10,"val2":20,"val3":30}
# printval(**d)


# cleaned_data => dict 



# {% url 'home' %}

# reverse('home')
# reverse_lazy("home")