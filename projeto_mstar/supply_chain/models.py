from django.db import models
from django.forms import DateTimeInput


class Local(models.Model):
    nome = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nome


class Mercadoria(models.Model):
    registro = models.IntegerField(unique=True)
    nome = models.CharField(max_length=250)
    fabricante = models.CharField(max_length=250)
    tipo = models.CharField(max_length=250)
    descricao = models.TextField()


    def __str__(self):
        return self.descricao


class Entrada(models.Model):
    quantidade = models.IntegerField()
    data = models.DateTimeField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)

class Saida(models.Model):
    quantidade = models.IntegerField()
    data = models.DateTimeField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    mercadoria = models.ForeignKey(Mercadoria, on_delete=models.CASCADE)

