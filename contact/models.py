from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)
# owner (foreign key)


# class Units(models.Model):
#     class Meta:
#         verbose_name = 'Unidade'

#     nome = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.nome


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'

    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


# class Category2(models.Model):
#     class Meta:
#         verbose_name = 'Uso do leito'
#         verbose_name_plural = 'Usos do leito'

#     nome = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.nome


class Contact(models.Model):
    class Meta:
        verbose_name = 'Agendamento'

    # unidade = models.ForeignKey(
    #     Units, on_delete=models.SET_NULL, blank=True, null=True)
    data_da_consulta = models.DateField(auto_now=False, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    categoria = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    nome_do_paciente = models.CharField(max_length=50, blank=True, null=True)
    hd = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True)
    anotacoes = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    # uso_do_leito = models.ForeignKey(
    #     Category2, on_delete=models.SET_NULL, blank=True, null=True)
    enviar_arquivo = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.cpf} {self.hd} {self.nome_do_paciente}'
