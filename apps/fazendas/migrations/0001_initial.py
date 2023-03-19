# Generated by Django 4.0.2 on 2022-03-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fazenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome da Fazenda')),
                ('cnpj', models.CharField(max_length=20, verbose_name='CNPJ')),
                ('responsavel', models.CharField(max_length=20, verbose_name='Responsável')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('tipoperfil', models.CharField(choices=[('BASICO', 'Básico'), ('INTERMEDIARIO', 'Intermediário'), ('MASTER', 'Master')], max_length=15)),
            ],
        ),
    ]