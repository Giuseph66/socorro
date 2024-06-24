# Generated by Django 5.0.3 on 2024-06-16 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socorro_app', '0004_cursos_class_alter_materias_class_materias'),
    ]

    operations = [
        migrations.AddField(
            model_name='materias_class',
            name='pai',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='socorro_app.cursos_class'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='materias_class',
            name='materias',
            field=models.CharField(max_length=200),
        ),
    ]