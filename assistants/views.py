from django.shortcuts import render,redirect, get_object_or_404
from .models import Assistants
from .forms import AssistantsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="user:loginUser")
def dashboard_assistants(request):
    informations = Assistants.objects.filter(authorized=request.user) 
    context = {
        "info":informations
    }
    
    return render(request, "dashboard_assistants.html", context)


@login_required(login_url="user:loginUser")
def add_assistant(request):
    form = AssistantsForm(request.POST or None)
    if form.is_valid():
        info = form.save(commit=False)
        info.authorized = request.user
        info.save()
        messages.info(request,"New Assistant Information Added Successfully")

        return redirect("assistants:dashboard_assistants")
    return render(request,"add_assistant.html", {"form":form})


@login_required(login_url="user:loginUser")
def detail_assistant(request,id):
    assistant=Assistants.objects.filter(id=id).first()
    return render(request,"detail_assistant.html",{"assistant":assistant})


@login_required(login_url="user:loginUser")
def update_assistant(request,id):
    assistant= get_object_or_404(Assistants, id=id)
    form= AssistantsForm(request.POST or None,instance=assistant)
    if form.is_valid():
        info=form.save(commit=False)
        info.authorized = request.user
        info.save()
        messages.success(request,"Assistant Information Has Been Updated Successfully")
        
        return redirect("assistants:dashboard_assistants")

    return render(request,"update_assistant.html",{"form":form})


@login_required(login_url="user:loginUser")
def delete_assistant(request,id):
    assistant= get_object_or_404(Assistants, id=id)
    assistant.delete()
    messages.success(request,"Assistant Successfully Deleted")
    return redirect("assistants:dashboard_assistants")