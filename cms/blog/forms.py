from django import forms
from blog.models import Category,Post
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist
class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    phone_number = forms.RegexField(required=False,regex = "^[6-9]\d{9}$")

    def clean(self):
        cleaned_data = super().clean()
        if not (cleaned_data.get('email') or cleaned_data.get('phone_number')):
            raise forms.ValidationError("Please enter either Email or Phone Number",code="invalid")

    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     if "edyoda" not in data:
    #         raise forms.ValidationError("Invalid domain",code ="invalid")
    #     return data


class RegisterForm(forms.Form):
    GENDER_CHOICES = [("M","Male"),("F","Female")]
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32,min_length=8,widget = forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32,min_length=8,widget = forms.PasswordInput)
    gender = forms.ChoiceField(choices = GENDER_CHOICES,widget = forms.RadioSelect)


# class PostForm(forms.Form):
#     statuses = [("D","Draft"),("P","Published")]
#     title = forms.CharField(max_length= 250)
#     content = forms.CharField(widget = forms.Textarea)
#     status = forms.ChoiceField(choices= statuses)
#     category = forms.ModelChoiceField(queryset = Category.objects.all())
#     image = forms.ImageField(required=False)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content','status','category','image']

    def clean_title(self):
        print("Getting here *********************************************************")
        title = self.cleaned_data.get('title')
        slug = slugify(title)
        try:
            post_obj = Post.objects.get(slug = slug)
            print(post_obj)
            raise forms.ValidationError("Title already exists",code ="Invalid")
        except ObjectDoesNotExist:
            return title 

    def clean_image(self):
        image = self.cleaned_data.get('image')
        # print(image.__dict__)
        return image



# TinyMCE



# Contact Us:
# Name
# Email
# Contact Number 
# Submit 