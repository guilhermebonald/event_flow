from django.contrib.auth.models import User
from django.db import models


class UserModel(User):
    # campos adicionais podem ser adicionados aqui
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class EventModel(models.Model):
    usuario = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data = models.DateField()
    tipo = models.CharField(max_length=255)
    presenca = models.CharField(max_length=255)
    comentarios = models.CharField(max_length=255)
