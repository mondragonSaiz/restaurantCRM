from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check if logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.succes(request, "You are now logged in.")
            return redirect('home')
        else:
            messages.success(request, "Error while logging in. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    

def logout_user(request):
    pass