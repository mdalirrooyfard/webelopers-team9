from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from contest import settings
from first.forms import SignupForm

def homepage(request):
    return render(request, 'Homepage.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # error1 = False
        # error2 = False
        # if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
        #     error1 = True
        # if authenticate(username=form.cleaned_data.get('username')) is not None:
        #     error2 = True
        # if error1 or error2:
        #     return render(request,'signup.html',{'form':form, 'error1':error1, 'error2':error2})
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
