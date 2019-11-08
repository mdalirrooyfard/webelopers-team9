from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from first.forms import SignupForm


def homepage(request):
    return render(request, 'Homepage.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
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
