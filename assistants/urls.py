from django.contrib import admin
from django.urls import path
from assistants import views
from . import views
app_name = "assistants"

urlpatterns = [
    path('dashboard_assistants/', views.dashboard_assistants, name="dashboard_assistants"),
    path('add_assistant/', views.add_assistant, name="add_assistant"),
    path('assistants/<int:id>', views.detail_assistant, name="detail_assistant"),
    path('delete_assistant/<int:id>', views.delete_assistant, name="delete_assistant"),
    path('update_assistant/<int:id>', views.update_assistant, name="update_assistant"),

]