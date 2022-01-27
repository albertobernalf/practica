# Generated by Django 3.2 on 2022-01-27 20:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sitios', '0007_auto_20220127_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.IntegerField()),
                ('consec', models.IntegerField()),
                ('fechaIngreso', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaSalida', models.DateTimeField(default=django.utils.timezone.now)),
                ('factura', models.IntegerField()),
                ('numcita', models.IntegerField()),
                ('salidaClinica', models.CharField(max_length=1)),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('dependenciasActual', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id1', to='sitios.dependencias')),
                ('dependenciasIngreso', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id0', to='sitios.dependencias')),
                ('dependenciasSalida', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id2', to='sitios.dependencias')),
            ],
        ),
    ]
