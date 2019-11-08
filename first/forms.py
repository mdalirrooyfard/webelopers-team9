from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from first.models import Course


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50,required=True)
    last_name = forms.CharField(max_length=50,required=True)
    username = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=300,required=True)
    password1 = forms.CharField(max_length=50,required=True)
    password2 = forms.CharField(max_length=50,required=True)


class CourseForm(ModelForm):
    class Meta:
        model= Course
        fields = ('department','name','course_number','group_number','teacher','start_time','end_time','first_day','second_day')

