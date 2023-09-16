from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('restaurant/<int:pk>', views.restaurant_record, name='restaurant'),
    path('delete_restaurant/<int:pk>', views.delete_restaurant, name="delete_restaurant"),

]