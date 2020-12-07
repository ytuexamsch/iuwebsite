#from django.contrib import admin
from django.urls import path
from . import views
app_name = "user"


urlpatterns = [
    path('register/', views.register,name="register"),
    path('loginUser/', views.loginUser,name="loginUser"),
    path('logoutUser/', views.logoutUser,name="logoutUser"),

]