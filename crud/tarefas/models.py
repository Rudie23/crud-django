from django.db import models


# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(max_length=256)
    feita = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
