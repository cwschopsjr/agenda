from django import forms
from contact.models import Contact
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):

    enviar_arquivo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'img/*',
            }
        )
    )

    class Meta:
        model = Contact
        fields = ('data_da_consulta', 'cpf', 'nome_do_paciente',
                  'hd', 'telefone', 'email', 'anotacoes', 'categoria',
                  'enviar_arquivo')

    def clean(self):
        cleaned_data = self.cleaned_data
        nome_do_paciente = cleaned_data.get('nome_do_paciente')
        hd = cleaned_data.get('hd')
        if nome_do_paciente == hd:
            msg = ValidationError(
                'O nome está igual ao hd',
                code='invalid'
            )
            self.add_error('nome_do_paciente', msg)
        return super().clean()


class RegisterForm(UserCreationForm):
    primeiro_nome = forms.CharField(
        required=True,
        min_length=3,
    )
    sobrenome = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'primeiro_nome', 'sobrenome', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

        return email
