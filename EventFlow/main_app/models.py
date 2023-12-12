from django.contrib.auth.models import User
from django.db import models


class Users(User):
    # campos adicionais podem ser adicionados aqui
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Events(models.Model):
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE)
    nome = models.DateField()
    data = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    presenca = models.CharField(max_length=255)
    comentarios = models.CharField(max_length=255)
