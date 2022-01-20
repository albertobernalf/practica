# Generated by Django 3.2 on 2022-01-17 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('clinico', '0001_initial'),
        ('sitios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AgendaMedica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lunes_desde', models.IntegerField()),
                ('lunes_hasta', models.IntegerField()),
                ('martes_desde', models.IntegerField()),
                ('martes_hasta', models.IntegerField()),
                ('miercoles_desde', models.IntegerField()),
                ('miercoles_hasta', models.IntegerField()),
                ('jueves_desde', models.IntegerField()),
                ('jueves_hasta', models.IntegerField()),
                ('viernes_desde', models.IntegerField()),
                ('viernes_hasta', models.IntegerField()),
                ('sabado_desde', models.IntegerField()),
                ('sabado_hasta', models.IntegerField()),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CitasEstados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CitasMedicas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numcita', models.IntegerField()),
                ('fecha_desde', models.DateField()),
                ('hora_desde', models.TimeField()),
                ('fecha_hasta', models.DateField()),
                ('hora_hasta', models.TimeField()),
                ('estado_actual', models.CharField(max_length=1)),
                ('id_AgendaMedica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='citasMedicas.agendamedica')),
                ('id_documento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.usuarios')),
                ('id_tipo_doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.tiposdocumento')),
            ],
        ),
        migrations.CreateModel(
            name='Cons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=70)),
                ('telefono', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ConsTipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ControlCitas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('estado', models.CharField(max_length=1)),
                ('id_cita', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='citasMedicas.citasmedicas')),
            ],
        ),
        migrations.CreateModel(
            name='ConsAgenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lunes_desde', models.IntegerField()),
                ('lunes_hasta', models.IntegerField()),
                ('martes_desde', models.IntegerField()),
                ('martes_hasta', models.IntegerField()),
                ('miercoles_desde', models.IntegerField()),
                ('miercoles_hasta', models.IntegerField()),
                ('jueves_desde', models.IntegerField()),
                ('jueves_hasta', models.IntegerField()),
                ('viernes_desde', models.IntegerField()),
                ('viernes_hasta', models.IntegerField()),
                ('sabado_desde', models.IntegerField()),
                ('sabado_hasta', models.IntegerField()),
                ('id_Agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='citasMedicas.agenda')),
                ('id_Cons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='citasMedicas.cons')),
                ('id_Especialidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.especialidades')),
            ],
        ),
        migrations.AddField(
            model_name='cons',
            name='id_ConsTipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='citasMedicas.constipo'),
        ),
        migrations.AddField(
            model_name='cons',
            name='id_ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.ciudades'),
        ),
        migrations.AddField(
            model_name='cons',
            name='id_depto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.departamentos'),
        ),
        migrations.AddField(
            model_name='agendamedica',
            name='id_ConsAgenda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='citasMedicas.consagenda'),
        ),
        migrations.AddField(
            model_name='agendamedica',
            name='id_Medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.medicos'),
        ),
    ]
