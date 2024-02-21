from django import forms
from contact.models import Contact
from django.shortcuts import render
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ('data_da_consulta', 'cpf', 'nome_do_paciente',
                  'hd', 'telefone', 'email', 'anotacoes', 'categoria')

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


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm()
    }

    return render(request, 'contact/create.html', context)
