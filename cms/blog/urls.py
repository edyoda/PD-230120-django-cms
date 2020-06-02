from django.urls import path,include
from blog.views import index,post_details
urlpatterns = [
    path('',index),
    path('blogs/<int:id>',post_details),    

]