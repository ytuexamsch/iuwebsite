#from django.contrib import admin
from django.urls import path
from classrooms import views
app_name = "classrooms"

urlpatterns = [
    path('dashboard_classrooms/', views.dashboard_classrooms, name="dashboard_classrooms"),
    path('add_classroom/', views.add_classroom, name="add_classroom"),
    path('update_classroom/<int:id>', views.update_classroom, name="update_classroom"),
    path('delete_classroom/<int:id>', views.delete_classroom, name="delete_classroom"),


]