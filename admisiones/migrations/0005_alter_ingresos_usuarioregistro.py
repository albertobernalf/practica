# Generated by Django 3.2 on 2022-01-28 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20220128_1632'),
        ('admisiones', '0004_alter_ingresos_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresos',
            name='usuarioRegistro',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.planta'),
        ),
    ]