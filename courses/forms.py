from django import forms
from .models import Courses
from django.core.exceptions import ValidationError
from django.forms import formset_factory
from .models import SameTimeCourses

class CoursesForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields=["course_code", "course_name", "course_capacity", "sixty_more", "slot_number", "lab_or_not",  "department",'desired_day', 'desired_slot']



class SameTimeCoursesForm(forms.ModelForm):
    class Meta:
        model = SameTimeCourses
        fields = ["course1_code" , "course2_code","cost"]
