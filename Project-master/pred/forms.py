from django import forms
from .models import prediction

class predform(forms.ModelForm):
    class Meta:
        model = prediction
        fields = '__all__'
    