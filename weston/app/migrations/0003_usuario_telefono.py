# Generated by Django 4.0.4 on 2022-06-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_activo_usuario_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(null=True, verbose_name='Telefono del usuario'),
        ),
    ]
