from django.db import models
from apps.fornecedores.models import Fornecedor
from apps.viveiros.models import TIPOS_UNIDADE

LISTA_CATEGORIA = (
    ('PESTICIDAS','Pesticidas'),
    ('INSUMO_CUSTO_INICIAL', 'Insumo/Custo Inicial'),
    ('RACAO', 'Ração'),
    ('VITAMINAS', 'Vitaminas'),
)

LISTA_CLASSIFICACAO = (
    ('FINAL', 'Final (Acabamento)'),
    ('INICIAL', 'Inicial'),
    ('INTERMEDIARIA', 'Intermediária'),
    ('NENHUMA', 'Nenhuma'),
)

LISTA_EMBALAGEM = (
    ('BALDE', 'Balde'),
    ('CAIXA', 'Caixa'),
    ('FRASCO', 'Frasco'),
    ('LATA', 'Lata'),
    ('SACO', 'Saco'),
    ('NENHUMA', 'Nenhuma'),
)

class Insumo(models.Model):
    descricao = models.CharField('Descrição', max_length=100)
    custo_un = models.DecimalField('Custo Médio (R$) por Unid. de Consumo', max_digits=7, decimal_places=2)
    un_consumo = models.CharField('Unidade de Consumo', max_length=15, choices=TIPOS_UNIDADE)
    categoria = models.CharField('Categoria', max_length=25, choices=LISTA_CATEGORIA)
    fornecedor = models.ForeignKey(Fornecedor, related_name="fornecedor", on_delete=models.CASCADE)
    marca = models.CharField('Marca', max_length=50)
    classificacao = models.CharField('Classificação', max_length=20, choices=LISTA_CLASSIFICACAO)
    validade = models.DateField('Validade', blank=True)
    peso_embalagem = models.DecimalField('Peso Embalagem', max_digits=5, decimal_places=2, blank=True)
    embalagem = models.CharField('Embalagem', max_length=20, choices=LISTA_EMBALAGEM, blank=True)
    ativo = models.BooleanField('Ativo', max_length=1)
    controla_estoque = models.BooleanField('Controla Estoque', max_length=1)
    permite_negativo = models.BooleanField('Permite Negativo', max_length=1)

    def __str__(self):
        return self.descricao
