from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.RegexField(regex = "^[6-9]\d{9}$")

# Contact Us:
# Name
# Email
# Contact Number 
# Submit 