# Generated by Django 3.2 on 2022-01-28 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_usuarios_usuarioregistro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiposdocumento',
            name='usuarioRegistro',
        ),
        migrations.RemoveField(
            model_name='tiposusuario',
            name='usuarioRegistro',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='usuarioRegistro',
        ),
    ]