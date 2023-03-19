from django.db import models

from apps.fornecedores.models import Fornecedor


class Cliente(Fornecedor):
    data_nasc = models.DateField('Data de Nascimento', blank=True)

