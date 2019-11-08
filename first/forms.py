from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50,required=True)
    last_name = forms.CharField(max_length=50,required=True)
    username = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=300,required=True)
    password1 = forms.CharField(max_length=50,required=True)
    password2 = forms.CharField(max_length=50,required=True)




