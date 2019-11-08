from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from first.forms import SignupForm, ContactForm


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
        form = ContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            return redirect('done')
        else:
            form.full_clean()
            return redirect('contact')
    else:
        form = ContactForm()
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
            pass
            return redirect('login')
    else:
        return render(request,"login.html")
