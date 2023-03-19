from django.db import models
from django.urls import reverse

LISTA_FORNECEDORES = (
    ("CLIENTE_EXTERNO", "Cliente Externo"),
    ("CLIENTE_INTERNO_FRIGORIFICO", "Cliente Interno/Frigorífico"),
    ("CLIENTE_BENEFICIAMENTO", "Cliente Beneficiamento"),
    ("FORNECEDOR_MATERIA_PRIMA", "Fornecedor de Matéria Prima"),
    ("FORNECEDOR_INSUMOS", "Fornecedor de Insumos"),
    ("LABORATORIO_LARVICULTURA", "Laboratório / Larvicultura"),
    ("PRESTADOR_SERVICO", "Prestador de Serviço"),
    ("FUNCIONARIO", "Funcionário")
)

TIPOS_PESSOA = (
    ("FISICA", "Física"),
    ("JURIDICA", "Jurídica"),
)

UF_SIGLA = [
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('EX', 'EX'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
]

#criar o parceiros

class Fornecedor(models.Model):
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100)
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj_cpf = models.CharField('CNPJ/CPF', unique=True, max_length=20)
    tipo_pessoa = models.CharField('Tipo de Pessoa', max_length=8, choices=TIPOS_PESSOA)
    ie_rg = models.CharField('IE/RG', max_length=20, blank=True)
    tipo_parceiro = models.CharField('Tipo de Fornecedor', max_length=30, choices=LISTA_FORNECEDORES)
    logradouro = models.CharField('Logradouro', max_length=100, blank=True)
    numero = models.CharField('Número', max_length=10, blank=True)
    bairro = models.CharField('Bairro', max_length=20, blank=True)
    cidade = models.CharField('Cidade', max_length=20, blank=True)
    estado = models.CharField('Estado', max_length=2, blank=True, choices=UF_SIGLA)
    cep = models.CharField('CEP', max_length=8, blank=True)
    responsavel = models.CharField('Responsável', max_length=100)
    contato = models.CharField('Contato', max_length=15)
    email = models.EmailField('E-mail', max_length=75, blank=True)

    def __str__(self):
       return self.razao_social

    def get_absolute_url(self):
        return reverse('home')


