from django import forms
from .models import Classrooms
from django.core.exceptions import ValidationError
from django.forms import formset_factory


class ClassroomsForm(forms.ModelForm):
    class Meta:
        model = Classrooms
        fields = [ "classroom_code", "classroom_name", "classroom_capacity", "lab_or_not"]
        