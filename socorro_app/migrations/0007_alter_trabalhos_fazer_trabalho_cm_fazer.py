# Generated by Django 5.0.3 on 2024-06-22 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socorro_app', '0006_trabalhos_fazer_curso_trab_trabalhos_fazer_trabalho_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalhos_fazer',
            name='trabalho_cm_fazer',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
