from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.


def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        confirm = form.cleaned_data.get("confirm")
        email=form.cleaned_data.get("email")
        

        newUser = User(username=username,first_name= first_name,email = email)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"You Have Successfully Registered!")
        return redirect("index")

    context = {
            "form" : form
        }
    return render(request,"register.html",context)


def loginUser(request):
    form =LoginForm(request.POST or None)
    context ={
        "form":form
    }
    if form.is_valid():
        username =form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,message="You Entered Wrong Username or Password!")
            return render(request,"loginUser.html",context)
        messages.success(request,"You Have Successfully Logged In!")
        login(request,user)
        return redirect("index")
    return render(request,"loginUser.html",context)


def logoutUser(request):
    logout(request)
    messages.warning(request,"You Are Logged Out!")
    return redirect("index")






