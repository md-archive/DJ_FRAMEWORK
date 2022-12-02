from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200)
    surname= forms.CharField(label="Apellidos", max_length=200)
    email = forms.CharField(label="Correo Electronico", max_length=100)
    password = forms.CharField(label="Contraseña", min_length=8, max_length=100)