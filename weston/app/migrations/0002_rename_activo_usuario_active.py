# Generated by Django 4.0.4 on 2022-06-04 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='activo',
            new_name='active',
        ),
    ]