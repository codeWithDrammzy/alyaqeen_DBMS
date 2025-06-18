from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from django import forms


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget= forms.PasswordInput)