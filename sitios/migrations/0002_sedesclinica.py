# Generated by Django 3.2 on 2022-01-27 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('sitios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SedesClinica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('contacto', models.CharField(max_length=50)),
                ('fechaRegistro', models.DateTimeField()),
                ('estadoReg', models.CharField(max_length=1)),
                ('ciudades_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.ciudades')),
                ('departamentos_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.departamentos')),
                ('usuarioRegistro_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.usuarios')),
            ],
        ),
    ]
