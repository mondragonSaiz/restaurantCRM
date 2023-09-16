# we import the models module from Django, which provides the tools and classes needed to define database models.
from django.db import models

# Create your models here.
# The model inherits from models.Model, which is the base class for all Django models.
class Restaurant(models.Model):
    # we first define a field named created_at of type DateTimeField. This field is automatically 
    # populated with the current date and time when a new Restaurant instance is created, thanks to auto_now_add=True.
    created_at = models.DateTimeField(auto_now_add=True)
    rest_name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    # we create a special method called __str__. It defines how instances of the Restaurant model should be represented as strings.
    # In this case, it returns a string that concatenates the rest_name and cuisine fields, making it easier to identify a restaurant
    # when working with Django's admin interface or other parts of your application.
    def __str__(self):
        return(f"{self.rest_name} {self.cuisine}")