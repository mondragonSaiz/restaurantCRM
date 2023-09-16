from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Restaurant

# we deine the SignUpForm class, which inherits from UserCreationForm. 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=80, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=80, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    # This Meta class inside the SignUpForm class is used to specify metadata about the form. 
    # It defines the model associated with the form (in this case - User, which is the built-in user model in Django)
    # and the fields that should be included in the form. These fields include the username, first name, last name, email, and password field
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # Initialize SignUpForm
    # This code is defining the __init__ method for the SignUpForm class,
    # which is a customization of the built-in Django UserCreationForm. 
    # The __init__ method is used to customize the form's appearance and behavior 
    # by modifying its field widgets, labels, and help text
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-light"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-light small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-light"><small>Enter the same password as before, for verification.</small></span>'	



# Add restaurant form
class AddRestaurantForm(forms.ModelForm):
    rest_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Name", "class": "form-control"}), label="")
    cuisine = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Restaurant type", "class": "form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}), label="")

    class Meta:
        model = Restaurant
        exclude = ("user",)