from django.db import models

from apps.viveiros.models import TIPOS_UNIDADE

TIPOS_NATUREZA = (
    ("FISICO_QUIMICO", "FÍSICO-QUÍMICO"),
    ("FITOPLANCTONS", "FITOPLANCTONS"),
    ("ZOOPLANCTONS", "ZOOPLANCTONS"),
    ("ANALISE_QUIMICA", "ANÁLISE-QUÍMICA"),
    ("ANALISE_CLINICA", "ANÁLISE-CLÍNICA"),
    ("FISIOLOGIA", "FISIOLOGIA"),
    ("ANALISE_PRESUNTIVA", "ANÁLISE-PRESUNTIVA"),
    ("BACTERIOLOGIA", "BACTERIOLOGIA"),
)
class Parametro(models.Model):
    descricao = models.CharField('Descrição', max_length=20)
    natureza = models.CharField('Natureza', max_length=20, choices=TIPOS_NATUREZA)
    un_medida = models.CharField('Unidade de Medida', max_length=12, choices=TIPOS_UNIDADE)
    permitido_min = models.IntegerField('Permitido Min.')
    permitido_max = models.IntegerField('Permitido Max.')
    ideal_max = models.IntegerField('Ideal Max.')
    ativo = models.BooleanField('Ativo', max_length=1)

    def __str__(self):
        return self.descricao