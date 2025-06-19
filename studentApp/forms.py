from django import forms
from .models import Student, Guardian

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['guardian']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'date_join': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }

class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = '__all__'
