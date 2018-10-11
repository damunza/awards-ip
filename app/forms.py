from django import forms
from .models import *

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['by','rating']