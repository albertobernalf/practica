from django.db import models

import usuarios

# Create your models here.



class TiposPlanta(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class PerfilesPlanta(models.Model):
    id=models.AutoField(primary_key=True)
    id_tipo_doc = models.ForeignKey('usuarios.TiposDocumento', default=1, on_delete=models.PROTECT, null=True)
    documento = models.IntegerField()
    id_perfilPlanta = models.ForeignKey('TiposPlanta', default=1, on_delete=models.PROTECT, null=True)
    estado = models.CharField(max_length=1)

    def __str__(self):
        return self.estado


class Planta(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    TIPO_CHOICES= (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    )
    id = models.AutoField(primary_key=True)
    id_tipo_doc = models.ForeignKey('usuarios.TiposDocumento', default=1, on_delete=models.PROTECT, null=True)
    documento =  models.IntegerField()
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, default ='L',choices=TIPO_CHOICES,)
    id_tiposPlanta = models.ForeignKey('TiposPlanta', default=1, on_delete=models.PROTECT, null=True)
    direccion = models.CharField(max_length=50)
    telefono  = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="fotos", null=True)
    estado = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre
