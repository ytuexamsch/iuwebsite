from django import forms
from .models import Assistants
from django.core.exceptions import ValidationError
from django.forms import formset_factory

class AssistantsForm(forms.ModelForm):
    class Meta:
        model=Assistants
        fields=["assistant_code", "assistant_name", "seniority","total_assignment" ,"undesired_days", "undesired_slots"]

