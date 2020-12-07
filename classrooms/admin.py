from django.contrib import admin
from .models import Classrooms
# Register your models here.
@admin.register(Classrooms)
class ClassroomsAdmin(admin.ModelAdmin):
    list_display=["classroom_code", "classroom_name", "classroom_capacity", "lab_or_not"]
    list_display_links=["classroom_code", "classroom_name"]
    search_fields=["classroom_name"]
    class Meta:
        model=Classrooms