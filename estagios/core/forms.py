from django import forms
from django.core.exceptions import ValidationError

class VagaForm(forms.Form):
    titulo = forms.CharField(max_length=150, error_messages={ 'required': 'Título é obrigatório' })
    empresa = forms.CharField(max_length=150, error_messages={ 'required': 'Empresa é obrigatória' })
    telefone = forms.CharField(max_length=20, error_messages={ 'required': 'Telefone é obrigatório' })
    email = forms.EmailField(max_length=150, error_messages={ 'required': 'Email é obrigatório' })
    descricao = forms.CharField(max_length=255, error_messages={ 'required': 'Descrição é obrigatória' })

    def clean_titulo(self):
        nome = self.cleaned_data['titulo']
        return nome.upper()

    def clean_empresa(self):
        empresa = self.cleaned_data['empresa']
        if len(empresa) < 2:
            raise ValidationError('Empresa precisa ter ao menos dois caracteres')
        return empresa.capitalize()

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if telefone.startswith('19'):
            return telefone
        raise ValidationError('DDD válido somente o 19')

    def clean_descricao(self):
        descricao = self.cleaned_data['descricao']
        if len(descricao) < 10:
            raise ValidationError('Descrição precisa ter ao menos dez caracteres')
        return descricao