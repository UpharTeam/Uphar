from django import forms
from admin1.models import doctors,patient,adminapp,Doctor_Department

class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model=adminapp
        fields='__all__'

class DoctorRegisterForm(forms.ModelForm):
    class Meta:
        model=doctors
        fields='__all__'

class PatientRegisterForm(forms.ModelForm):
    class Meta:
        model=patient
        fields='__all__'

class DoctorDEpForm(forms.ModelForm):
    class Meta:
        model = Doctor_Department
        fields='__all__'