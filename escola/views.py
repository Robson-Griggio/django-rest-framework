from django.db import models

# Create your views here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.CharField(max_length=30)
    nome = models.DateField()

    def __str__(self):
        return self.nome

