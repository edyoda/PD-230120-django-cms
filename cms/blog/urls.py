from django.urls import path,include
from blog.views import index,post_details,contact_us_form_view,register_form_view,post_form_view,post_update_form_view
urlpatterns = [
    path('',index,name = "home"),
    path('blogs/<int:id>',post_details,name ="post-detail"), 
    path('contact',contact_us_form_view),
    path('register',register_form_view),
    path('post',post_form_view),
    path('post/<int:id>',post_update_form_view),
]