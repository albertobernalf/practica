from django.db import models

from  usuarios.models import TiposDocumento, Usuarios

# Create your models here.

class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    nombre = models.CharField(max_length= 30)

    def __str__(self):
        return self.nombre

class ConsTipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Cons(models.Model):
    id = models.AutoField(primary_key=True)
    id_ConsTipo = models.ForeignKey('ConsTipo', on_delete= models.PROTECT, null=True)
    id_depto = models.ForeignKey('sitios.departamentos', on_delete= models.PROTECT, null=True)
    id_ciudad = models.ForeignKey('sitios.CIudades', on_delete= models.PROTECT, null= True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class ConsAgenda(models.Model):

    id = models.AutoField(primary_key=True)
    id_Agenda = models.ForeignKey('Agenda', on_delete= models.PROTECT, null= True)
    id_Cons = models.ForeignKey('Cons', on_delete= models.PROTECT, null= True)
    id_Especialidad =  models.ForeignKey('clinico.Especialidades', on_delete= models.PROTECT, null= True)
    lunes_desde = models.IntegerField()
    lunes_hasta = models.IntegerField()
    martes_desde = models.IntegerField()
    martes_hasta = models.IntegerField()
    miercoles_desde = models.IntegerField()
    miercoles_hasta = models.IntegerField()
    jueves_desde = models.IntegerField()
    jueves_hasta = models.IntegerField()
    viernes_desde = models.IntegerField()
    viernes_hasta = models.IntegerField()
    sabado_desde = models.IntegerField()
    sabado_hasta = models.IntegerField()



    def __integer__(self):
        return (self.id)


class AgendaMedica(models.Model):
    id = models.AutoField   (primary_key=True)
    id_ConsAgenda = models.ForeignKey('ConsAgenda', on_delete=models.PROTECT, null=True)
    id_Medico = models.ForeignKey('clinico.Medicos', on_delete=models.PROTECT, null=True)
    lunes_desde = models.IntegerField()
    lunes_hasta = models.IntegerField()
    martes_desde = models.IntegerField()
    martes_hasta = models.IntegerField()
    miercoles_desde = models.IntegerField()
    miercoles_hasta = models.IntegerField()
    jueves_desde = models.IntegerField()
    jueves_hasta = models.IntegerField()
    viernes_desde = models.IntegerField()
    viernes_hasta = models.IntegerField()
    sabado_desde = models.IntegerField()
    sabado_hasta = models.IntegerField()
    estado = models.CharField(max_length=1)


class CitasEstados(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class CitasMedicas(models.Model):
    id = models.AutoField(primary_key=True)
    numcita = models.IntegerField()
    id_AgendaMedica = models.ForeignKey('AgendaMedica', on_delete=models.PROTECT, null=True)
    fecha_desde = models.DateField()
    hora_desde  = models.TimeField()
    fecha_hasta = models.DateField()
    hora_hasta = models.TimeField()
    id_tipo_doc = models.ForeignKey('usuarios.TiposDocumento', on_delete=models.PROTECT, null=True)
    id_documento = models.ForeignKey('usuarios.Usuarios', on_delete=models.PROTECT, null=True)
    estado_actual = models.CharField(max_length=1)




class ControlCitas(models.Model):
    id = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey('CitasMedicas', on_delete=models.PROTECT, null=True)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=1)
