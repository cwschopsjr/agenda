from django.db import models
from django.utils import timezone

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreign key)


class Units(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Category(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Category2(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Contact(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    anotacoes = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    unidade = models.ForeignKey(
        Units, on_delete=models.SET_NULL, blank=True, null=True)
    tipo_de_leito = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    uso_do_leito = models.ForeignKey(
        Category2, on_delete=models.SET_NULL, blank=True, null=True)
    enviar_arquivo = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
