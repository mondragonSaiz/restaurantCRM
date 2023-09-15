from django.db import models

# Create your models here.
class Restaurant(model.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    rest_name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.rest_name} {self.cusine}")