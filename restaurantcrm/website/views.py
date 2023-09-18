from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRestaurantForm
from .models import Restaurant

# Create your views here.
def home(request):
    # we get all of the objects from db
    restaurants = Restaurant.objects.all()
    # check if incoming request method is POST type
    if request.method == 'POST':
     #  extracting the values submitted in the POST request with the keys 'username' and 'password'.
     #  It expects that a form with fields named 'username' and 'password' was submitted.
        username = request.POST['username']
        password = request.POST['password']
    # Django's authenticate function is used to check the submitted username and password against the user authentication backend.
    # If the credentials are valid, it returns a user object, if not it returns None
        user = authenticate(request, username=username, password=password)
        # If the authenticate function returns a user object (user is not None), it means the login was successful. 
        # The code logs in the user using Django's login function, which sets the user in the current session. 
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('home')
        else:
            messages.success(request, "Error while logging in. Please try again.")
            return redirect('home')
    # If the request method is not POST (it's a GET request), this block of code is executed.
    # It renders the 'home.html' template and passes a context variable restaurants to it. 
    else:
        return render(request, 'home.html', {'restaurants': restaurants})
    
# log the user out of their current session.
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        # Django form class SignUpForm is instantiated with the data from the POST request.
        form = SignUpForm(request.POST)
        # we check if the submitted form data is valid according to the rules defined in the SignUpForm class.
        if form.is_valid():
            # If the form is valid, it saves the user registration data to the database.
            form.save()
            #  extract the cleaned data from the form fields for username and password.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have succesfully registered.")
            return redirect ('home')
    # If the request method is not POST (it's a GET request), this next block of code gets executed. 
    # It creates a new instance of the SignUpForm to display an empty registration form and renders 
    # the 'register.html' template with this form as context data.
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    # This last line  provides a fallback case to render the 'register.html' template with the form in case 
    # neither the POST nor the GET condition is met. This ensures that the form is always available for
    # rendering in the template.
    return render(request, 'register.html', {'form': form})


def restaurant_record(request, pk):
    # check if user is authenticated (logged in)
    if request.user.is_authenticated:
        # gets specified restaurant with primary key from db
        restaurant_record = Restaurant.objects.get(id=pk)
        # renders the restaurant.html with the restaurant_record as context data
        return render(request, 'restaurant.html', {'restaurant_record': restaurant_record})
    else:
        #if user not logged in an error message is passed to display and user is redirected to home
        messages.success(request, "You must be logged in to view the specified restaurant")
        return redirect('home')
    

def delete_restaurant(request, pk):
    if request.user.is_authenticated:
        # gets specified restaurant with primary key from db
        delete_rest = Restaurant.objects.get(id=pk)
        # we use the method detele() on our restuarant object
        delete_rest.delete()
        messages.success(request, "Restaurant deleted succesfully.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete restautant.")
        return redirect('home')

def add_restaurant(request):
    # here we create an instance of the AddRestaurantForm form is created,
    #  either with the data from a POST request (if available) or as an empty form (if it's a GET request)
    form = AddRestaurantForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                # If the form is valid, it saves the restaurant data to the database using the form.save() method.
                # The saved restaurant object is assigned to the variable add_restaurant.
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
        # here we create an instance of the AddRestaurantForm form is created, 
        # either with the data from a POST request (if available) or as an empty form 
        # (if it's a GET request). Additionally, the instance parameter is set to the 
        # existing restaurant object, which pre-fills the form with the restaurant's current data for editing.
        form = AddRestaurantForm(request.POST or None, instance=existing_restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, "Restaurant updated succesfully.")
            return redirect('home')
        # If request method is POST but the form is not valid, or if it's a GET request, 
        # the code renders the 'update_restaurant.html' template with the form as context data.
        # This allows the user to view and edit the restaurant's information.
        return render(request, 'update_restaurant.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to update restautant.")
        return redirect('home')