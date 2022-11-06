from django import forms
from .models import Task_db

class Listform(forms.ModelForm):
    class Meta:
        model = Task_db
        fields = ['title','task','date']