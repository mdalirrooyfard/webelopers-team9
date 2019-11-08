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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('done')
    else:
        form = ContactForm()
    return render(request,"contact.html",{'form':form})
