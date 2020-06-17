from django.urls import path,include
from blog.views import index,post_details,contact_us_form_view,register_form_view,post_form_view,post_update_form_view
from blog.views import HomeView,PostView,PostCreateView,PostListView,PostDetailView,AboutUs
urlpatterns = [
    path('',PostListView.as_view(),name = "home"),
    # path('blogs/<slug:slug>',RedirectPost.as_view()), 
    path('blogs/<slug:slug>',PostDetailView.as_view(),name ="post-detail"), 
    
    path('contact',contact_us_form_view),
    # path('register',register_form_view),
    path('post',PostCreateView.as_view()),
    path('post/<int:id>',post_update_form_view),
    path('about-us',AboutUs.as_view()),

]