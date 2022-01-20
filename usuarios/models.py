from django.db import models

# Create your models here.


class TiposDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    abreviatura= models.CharField(max_length=2)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class TiposUsuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
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
    genero = models.CharField(max_length=1, default ='L',choices=TIPO_CHOICES,)
    id_tiposUsuario = models.ForeignKey('usuarios.TiposUsuario', default=1, on_delete=models.PROTECT, null=True)
    direccion = models.CharField(max_length=50)
    telefono  = models.CharField(max_length=20)
    contacto  = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="fotos", null=True)
    id_centro =  models.ForeignKey('sitios.Centros', default=1, on_delete=models.PROTECT, null=True)
    estado = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre