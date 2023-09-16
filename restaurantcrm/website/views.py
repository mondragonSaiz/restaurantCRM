from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRestaurantForm
from .models import Restaurant

# Create your views here.
def home(request):
    # we get all of the objects from db
    restaurants = Restaurant.objects.all()
    # check if logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('home')
        else:
            messages.success(request, "Error while logging in. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'restaurants': restaurants})
    

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # auth and log in logic
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have succesfully registered.")
            return redirect ('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def restaurant_record(request, pk):
    if request.user.is_authenticated:
        #check specified restaurant in db
        restaurant_record = Restaurant.objects.get(id=pk)
        return render(request, 'restaurant.html', {'restaurant_record': restaurant_record})
    else:
        messages.success(request, "You must be logged in to view the specified restaurant")
        return redirect('home')
    

def delete_restaurant(request, pk):
    if request.user.is_authenticated:
        delete_res = Restaurant.objects.get(id=pk)
        delete_res.delete()
        messages.success(request, "Restaurant deleted succesfully.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete restautant.")
        return redirect('home')

def add_restaurant(request):
    form = AddRestaurantForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_restaurant = form.save()
                messages.success(request, "Restaurant added succesfully.")
                return redirect('home')
        return render(request, 'add_restaurant.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add restaurant.")
        return redirect('home')

def update_restaurant(request, pk):
    if request.user.is_authenticated:
        existing_restaurant = Restaurant.objects.get(id=pk)
        form = AddRestaurantForm(request.POST or None, instance=existing_restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, "Restaurant updated succesfully.")
            return redirect('home')
        return render(request, 'update_restaurant.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to update restautant.")
        return redirect('home')