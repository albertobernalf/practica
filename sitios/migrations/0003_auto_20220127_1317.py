# Generated by Django 3.2 on 2022-01-27 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0002_sedesclinica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sedesclinica',
            old_name='ciudades_id',
            new_name='ciudades',
        ),
        migrations.RenameField(
            model_name='sedesclinica',
            old_name='departamentos_id',
            new_name='departamentos',
        ),
        migrations.RenameField(
            model_name='sedesclinica',
            old_name='usuarioRegistro_id',
            new_name='usuarioRegistro',
        ),
    ]
