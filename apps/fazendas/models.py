from django.db import models
from apps.users.models import Usuario

PERFIL_USUARIO = (
    ("BASICO", "Básico"),
    ("INTERMEDIARIO", "Intermediário"),
    ("MASTER", "Master"),
)

class Fazenda(models.Model):
    nome = models.CharField('Nome da Fazenda', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=20)
    responsavel = models.CharField('Responsável', max_length=20)
    endereco = models.CharField('Endereço', max_length=50)
    user = models.OneToOneField(Usuario, on_delete=models.PROTECT)
    tipoperfil = models.CharField(max_length=15, choices=PERFIL_USUARIO)

    def __str__(self):
        return self.nome









