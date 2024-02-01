from .models import todo
from django import forms

class todoform(forms.ModelForm):
    class Meta:
        model=todo
        fields=['task','priority','date']