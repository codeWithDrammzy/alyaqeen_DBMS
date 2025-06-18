from django import forms
from .models import*

from django import forms
from .models import Teacher, Subject

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'



class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'

class AcademicSessionForm(forms.ModelForm):
    class Meta:
        model = AcademicSession
        fields = ['name']