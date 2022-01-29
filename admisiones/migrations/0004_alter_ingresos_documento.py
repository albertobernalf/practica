# Generated by Django 3.2 on 2022-01-28 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuarios_documento'),
        ('admisiones', '0003_auto_20220128_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresos',
            name='documento',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Documento', to='usuarios.usuarios'),
        ),
    ]