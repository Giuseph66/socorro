# Generated by Django 5.0.3 on 2024-06-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socorro_app', '0007_alter_trabalhos_fazer_trabalho_cm_fazer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalhos_fazer',
            name='trabalho_cm_fazer',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
