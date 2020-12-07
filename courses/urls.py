from django.contrib import admin
from django.urls import path
from courses import views
from . import views
app_name = "courses"

urlpatterns = [
    path('', views.index, name = "index"),
    path('dashboard_courses/', views.dashboard_courses, name = "dashboard_courses"),
    path('add_course/', views.add_course, name = "add_course"),
    path('courses/<int:id>', views.detail_course, name="detail_course"),
    path('add_sametime_course/', views.add_sametime_course, name = "add_sametime_course"),
    path('dashboard_sametime_courses/', views.dashboard_sametime_courses, name = "dashboard_sametime_courses"),
    path('update_course/<int:id>', views.update_course, name="update_course"),
    path('delete_course/<int:id>', views.delete_course, name="delete_course"),
    path('delete_sametime_course/<int:id>', views.delete_sametime_course, name="delete_sametime_course"),

]