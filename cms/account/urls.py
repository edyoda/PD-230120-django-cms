from django.contrib import admin
from django.urls import path,include
from account.views import SignUpView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("register",SignUpView.as_view()), 
    # path("login",LoginView.as_view(template_name="account/login.html")),
    path("",include("django.contrib.auth.urls")),
    

]
