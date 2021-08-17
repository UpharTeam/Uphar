from django import forms
from .models import cat,com,inc

class catform(forms.ModelForm):
    class Meta:
        model=cat   
        fields="__all__"

class comform(forms.ModelForm):
    class Meta:
        model=com   
        fields="__all__"
class incform(forms.ModelForm):
    class Meta:
        model=inc   
        fields="__all__"
