from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateNewList(forms.Form):
    name = forms.CharField(label="ToDo List Name", max_length=200)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = User
        fields = ["firstname", "lastname", "email", "username", "password1", "password2"]
        