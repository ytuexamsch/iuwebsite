"""schedule_iu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('courses/', include("courses.urls")),
    path('user/', include("user.urls")),
    path('classrooms/', include("classrooms.urls")),  
    path('assistants/', include("assistants.urls")),    
    path('initial_load', views.initial_load, name="initial_load"),
    path('exam_timetable_results', views.exam_schedule),
    path('supervisor_assignment_results', views.assistant_schedule),
    path('main_dashboard', views.main_dashboard),
]

