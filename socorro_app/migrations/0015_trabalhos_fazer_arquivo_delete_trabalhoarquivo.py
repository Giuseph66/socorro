# Generated by Django 5.0.3 on 2024-06-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socorro_app', '0014_alter_trabalhos_fazer_trabalho_cm_pronto'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabalhos_fazer',
            name='arquivo',
            field=models.FileField(default='', upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TrabalhoArquivo',
        ),
    ]
