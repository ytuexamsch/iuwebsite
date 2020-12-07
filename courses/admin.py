from django.contrib import admin
from .models import Courses
# Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display=["course_code","course_name","course_capacity","sixty_more"]
    list_display_links=["course_code", "course_name"]
    search_fields=["course_name"]
    class Meta:
        model=Courses