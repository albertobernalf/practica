# Generated by Django 3.2 on 2022-01-28 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0008_auto_20220128_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dependencias',
            name='usuarioRegistro',
        ),
        migrations.RemoveField(
            model_name='dependenciasactual',
            name='usuarioRegistro',
        ),
    ]
