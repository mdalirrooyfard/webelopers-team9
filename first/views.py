from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from first.forms import SignupForm


def homepage(request):
    return render(request, 'Homepage.html')


def signup(request):
    # first_name = 'NaN'
    # last_name = 'NaN'
    # username = 'NaN'
    # email = 'NaN'
    # password1 = 'Nan'
    # password2
    if request.method == 'POST':
        form = SignupForm(request.POST)
        #print(request)
        if form.is_valid():
            #print('valid')
            user = form.save()
            user.refresh_from_db()
            user.save()
            #return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
