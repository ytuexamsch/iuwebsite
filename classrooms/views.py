from django.shortcuts import render, redirect, get_object_or_404
from .models import Classrooms
from .forms import ClassroomsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required






@login_required(login_url="user:loginUser")
def dashboard_classrooms(request):
    informations = Classrooms.objects.filter(authorized = request.user) 
    context = {
        "info":informations
    }
    
    return render(request, "dashboard_classrooms.html", context)



@login_required(login_url="user:loginUser")
def add_classroom(request):
    form = ClassroomsForm(request.POST or None)
    if form.is_valid():
        info = form.save(commit=False)
        info.authorized = request.user
        info.save()
        messages.info(request,"New Classroom Added Successfully")

        return redirect("classrooms:dashboard_classrooms")
    return render(request,"add_course.html",{"form":form})


@login_required(login_url="user:loginUser")
def update_classroom(request,id):
    classroom = get_object_or_404(Classrooms, id=id)
    form = ClassroomsForm(request.POST or None,instance=classroom)
    if form.is_valid():
        info=form.save(commit=False)
        info.authorized = request.user
        info.save()
        messages.success(request,"Classroom Information Updated Successfully")
        
        return redirect("classrooms:dashboard_classrooms")

    return render(request,"update_classroom.html",{"form":form})



@login_required(login_url="user:loginUser")
def delete_classroom(request, id):
    classroom= get_object_or_404(Classrooms, id=id)
    classroom.delete()
    messages.success(request,"Classroom Successfully Deleted")
    return redirect("classrooms:dashboard_classrooms")