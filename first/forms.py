from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,required=True)
    last_name = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=300,required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2',)


class ContactForm(forms.Form):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(min_length=10,max_length=250,required=True)


