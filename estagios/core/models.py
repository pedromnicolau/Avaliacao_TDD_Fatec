from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

class VagaModel(models.Model):
    titulo = models.CharField('Título da Vaga', max_length=150, blank=False)
    empresa = models.CharField('Empresa', max_length=150, validators=[MinLengthValidator(2)], blank=False)
    telefone = models.CharField('Telefone', max_length=20, blank=False)
    email = models.CharField('Email', max_length=150, blank=False)
    descricao = models.CharField('Descrição', max_length=255, validators=[MinLengthValidator(10)], blank=False)

    def __str__(self):
        return self.titulo
