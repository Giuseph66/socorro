# Generated by Django 5.0.3 on 2024-06-06 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materias_clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materias', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('cell', models.IntegerField()),
                ('saldo', models.IntegerField()),
                ('chave_pix', models.CharField(max_length=200)),
                ('gmail', models.EmailField(max_length=500)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trabalhos_fazer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quem_pediu_fazer', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=100)),
                ('valor_afazer', models.IntegerField()),
                ('pago', models.CharField(max_length=200)),
                ('fazer_materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socorro_app.materias_clas')),
            ],
        ),
        migrations.CreateModel(
            name='Transações',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quem_compro', models.CharField(max_length=200)),
                ('quem_pago', models.CharField(max_length=200)),
                ('valor_pago', models.IntegerField()),
                ('qual_trabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socorro_app.trabalhos_fazer')),
            ],
        ),
    ]
