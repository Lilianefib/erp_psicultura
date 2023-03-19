from django.db import models

TIPOS_PLANO_CONTAS = (
    ("FIXO", "FIXO"),
    ("VARIAVEL", "VARIÁVEL"),
)

class PlanoConta(models.Model):
    codigo = models.CharField('Código', max_length=20)
    descricao = models.CharField('Descrição', max_length=50)
    tipo_plano_contas = models.CharField('Tipo',max_length=8, choices=TIPOS_PLANO_CONTAS)

    def __str__(self):
        return self.codigo + ' - ' + self.descricao

class Custo(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    plano_contas = models.ForeignKey(PlanoConta, related_name="plano_contas", on_delete=models.CASCADE)
    custo_medio = models.DecimalField('Custo Médio (Compra, Consumo)', max_digits=10, decimal_places=2, blank=True)
    ativo = models.BooleanField('Ativo', max_length=1)

    def __str__(self):
        return self.descricao
