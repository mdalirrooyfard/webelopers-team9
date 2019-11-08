from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from contest import settings
from first.forms import SignupForm, CourseForm
from first.models import Course


def homepage(request):
    return render(request, 'Homepage.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        error1 = False
        error2 = False
        if form.is_valid():
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                error1 = True
            if len (User.objects.filter(username=form.cleaned_data['username'])) > 0:
                error2 = True
            if error1 or error2:
                return render(request,'signup.html',{'form':form, 'error1':error1, 'error2':error2})
            user = User(username=form.cleaned_data['username'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name']
                        , email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            user.save()
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def contact(request):
    title = ""
    email = ""
    text = ""
    if request.method == "POST":
        title = request.POST['title']
        email = request.POST['email']
        text = request.POST['text']
        if 10 <=len(text)<=250:
            send_mail(
                title,
                text + email,
                settings.EMAIL_HOST,
                ['webe19lopers@gmail.com'],
                fail_silently=False,
            )
            return redirect('done')
        else:
            return redirect('contact')
    else:
        return render(request,'contact.html')


def Login(request):
    username = ""
    password = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{"error":True})
    else:
        return render(request,"login.html",{"error":False})


def Logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    user = request.user
    return render(request, 'profile.html', {'first_name':user.first_name, 'last_name':user.last_name, 'username':user.username})


def setting(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if len(first_name) > 0 or len(last_name) > 0:
            user = request.user
            print(user.first_name)
            if len(first_name) > 0:
                user.first_name = first_name
            if len(last_name):
                user.last_name = last_name
            user.save()
        return redirect('profile')

    else:
        return render(request,'settings.html')


def new_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            course.save()
            return redirect('panel')
        return redirect('new_course')
    else:
        form = CourseForm()
        return render(request,"new_course.html", {"form":form})


def Courses(request):
    courses = Course.objects.all()
    return render(request,"cources.html",{"courses":courses})

