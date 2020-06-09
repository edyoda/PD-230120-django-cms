from django.db import models
from django.utils.text import slugify

# Create your models here.


# 1. CRUD on blog 
# 2. Auth :
#     1. Only author will login and authors can perform CRUD 
#     2. Reader and Autor
# 3. Not loggedin user can view only 3 blogs 
# 4. Search 
# 5. Edit profile, Login,Logout,Reset Password,Change Password  
# 6. Adding a rich text editor 


# Blog:
# 1. Title 
# 2. Category 
# 3. Image 
# 4. Content 
# 5. Author 
# 6. Status Draft/Published 
# 7. Published Date 
# 8. Author Description 
# 9. Category description

# Category:
# id 
# name 
# description 

# Author:
# id 
# username
# Password
# email 
# name 
# about 
# profile_pic 
# domain 

# Post:
# id
# Title : CharField 
# image 
# status 
# pub_date 
# content : TextField 
# category 
# author 

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = [("D","Draft"),("P","Published")]

    title = models.CharField(max_length = 250)
    content = models.TextField()
    status = models.CharField(max_length=1,choices=statuses,default="D")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="categories")
    image = models.ImageField(upload_to="blog/",blank = True)
    slug = models.SlugField(unique= True,blank = True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):

        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

# slugify(title) => slug => object 

#Get all the objects:
# Post.objects.all() => Queryset 

# Get one object :
# Post.objcets.get(field__lookkuptype = "value"):
#     Object Does not exist
#     Multiple objects returned 

# Post.objcets.filter(category = cat_obj)
# Post.objects.filter(category__name = "name")

# obj.modelname_set.all()
# obj.related_name.all()

# urls: 
#   localhost:8000/blogs


# def view(request):
#     obj = Post.objects.all()
#     return HTTPResponse 


# https://codepen.io/learninguser/full/WNbBXWN





