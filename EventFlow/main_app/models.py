from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    # campos adicionais podem ser adicionados aqui
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Car(models.Model):
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    ano = models.IntegerField()
    tipo = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    quilometragem = models.IntegerField()
