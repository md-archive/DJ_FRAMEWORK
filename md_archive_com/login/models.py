from django.db import models


class username(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class items(models.Model):
    username = models.ForeignKey(username, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()


class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=20)
    Segundo_nombre = models.CharField(max_length=20)
    Primer_apellido = models.CharField(max_length=20)
    Segundo_apellido = models.CharField(max_length=30)
    Cuenta_creada = models.DateTimeField(null=True, blank=True)
    Cuenta_activa = models.BooleanField(default=True)

    def __str__(self):
        return self.text
