# Generated by Django 3.2.18 on 2023-03-09 01:28

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificao', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificao', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='servico', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificao', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('bio', models.TextField(max_length=255, verbose_name='Biografia')),
                ('foto', stdimage.models.StdImageField(force_min_size=False, upload_to='equipe', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto')),
                ('facebook', models.CharField(max_length=200, verbose_name='Facebook')),
                ('twitter', models.CharField(max_length=200, verbose_name='Twitter')),
                ('instagram', models.CharField(max_length=200, verbose_name='Instagram')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]
