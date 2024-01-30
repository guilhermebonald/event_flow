from main_app.models import UserModel
from django.db import models


class EventModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data = models.DateField()
    tipo = models.CharField(max_length=255)
    presenca = models.CharField(max_length=255)
    comentarios = models.CharField(max_length=255)
