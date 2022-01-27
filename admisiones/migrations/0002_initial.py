# Generated by Django 3.2 on 2022-01-27 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planta', '0002_auto_20220127_1511'),
        ('sitios', '0007_auto_20220127_1439'),
        ('clinico', '0003_diagnosticos_estadossalida'),
        ('admisiones', '0001_initial'),
        ('usuarios', '0002_auto_20220127_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresos',
            name='dxActual',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id4', to='clinico.diagnosticos'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='dxIngreso',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id3', to='clinico.diagnosticos'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='dxSalida',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id5', to='clinico.diagnosticos'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='estadoSalida',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.estadossalida'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='medicoActual',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id7', to='planta.planta'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='medicoIngreso',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id6', to='planta.planta'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='medicoSalida',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id8', to='planta.planta'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='sedesClinica',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.sedesclinica'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='serviciosActual',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id10', to='clinico.servicios'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='serviciosIng',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id9', to='clinico.servicios'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='serviciosSalida',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id11', to='clinico.servicios'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='tipoDoc',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.tiposdocumento'),
        ),
        migrations.AddField(
            model_name='ingresos',
            name='usuarioRegistro',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.usuarios'),
        ),
    ]
