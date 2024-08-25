from django import forms
from .models import register

class regif(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'