from django.db import models

TIPOS_UNIDADE = (
    ("CEL_ML", "cel/ml"),
    ("CENTIMETROS", "Centímetros"),
    ("DOSE", "Dose"),
    ("GRAMAS", "Gramas"),
    ("GRAUS", "Graus Celsios"),
    ("HECTARE", "Hectare"),
    ("LIBRA", "Libra"),
    ("METRO_CUBICO", "Metro Cúbico"),
    ("METRO","Metro Quadrado"),
    ("METROS", "Metros"),
    ("MG_L", "mg/l"),
    ("MILILITRO", "Mililitro"),
    ("PERCENTUAL", "Percentual"),
    ("PPM", "ppm"),
    ("PPT", "ppt"),
    ("QUILOS", "Quilos"),
    ("SEGUNDOS", "Segundos"),
    ("TONELADA", "Tonelada"),
    ("UFC_ML", "UFC/ml"),
)

TIPOS_VIVEIROS= (
    ("BERCARIO", "Berçário"),
    ("CANAL", "Canal"),
    ("FINAL", "Final/Engorda"),
    ("INTERMEDIARIO", "Intermediário"),
    ("REPRODUTOR", "Reprodutor"),
    ("SETOR", "Setor"),
)

class Viveiro(models.Model):
    descricao = models.CharField('Descrição', max_length=20)
    tipo = models.CharField('Tipo', max_length=13, choices=TIPOS_VIVEIROS)
    area = models.CharField('Área', max_length=15)
    un_medida = models.CharField('Unidade de Medida', max_length=12, choices=TIPOS_UNIDADE)
    fator_densidade = models.CharField('Fator Densidade', max_length=8)
    setor = models.CharField('Setor', max_length=20)
    ciclo = models.CharField('Ciclo', max_length=15)
    estado = models.CharField('Estado', max_length=15)
    ativo = models.BooleanField('Ativo', max_length=1)


    def __str__(self):
        return self.descricao
