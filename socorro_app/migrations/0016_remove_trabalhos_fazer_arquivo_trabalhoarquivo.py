# Generated by Django 5.0.3 on 2024-06-26 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socorro_app', '0015_trabalhos_fazer_arquivo_delete_trabalhoarquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabalhos_fazer',
            name='arquivo',
        ),
        migrations.CreateModel(
            name='TrabalhoArquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='uploads/')),
                ('trabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arquivos', to='socorro_app.trabalhos_fazer')),
            ],
        ),
    ]
