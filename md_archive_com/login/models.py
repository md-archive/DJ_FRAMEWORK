from django.db import models
from django.contrib.auth.models import User
from django import forms

class username(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class items(models.Model):
    username = models.ForeignKey(username, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()


class Usuario(models.Model):
    title = models.CharField(max_length=100, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    password = forms.HiddenInput()
    primer_nombre = models.CharField(max_length=20)
    Segundo_nombre = models.CharField(max_length=20)
    Primer_apellido = models.CharField(max_length=20)
    Segundo_apellido = models.CharField(max_length=30)

    def __str__(self):
        return self.title + '- by ' + self.user.username
