from django import forms
from contact.models import Contact
from django.shortcuts import render
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('data_da_consulta', 'nome_do_paciente')


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
