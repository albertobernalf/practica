from django.db import models

# Create your models here.


class Departamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Ciudades(models.Model):
        id = models.AutoField(primary_key=True)
        id_departamento = models.ForeignKey('sitios.Departamentos', default=1, on_delete=models.PROTECT, null=True)
        nombre = models.CharField(max_length=30)

        def __str__(self):
            return self.nombre

class Centros(models.Model):
            id = models.AutoField(primary_key=True)
            nombre = models.CharField(max_length=30)
            id_departamento = models.ForeignKey('sitios.Departamentos', default=1, on_delete=models.PROTECT, null=True)
            id_ciudad = models.ForeignKey('sitios.Ciudades', default=1, on_delete=models.PROTECT, null=True)
            direccion = models.CharField(max_length=50)
            telefono = models.CharField(max_length=20)
            contacto = models.CharField(max_length=50)
            estado = models.CharField(max_length=1)


            def __str__(self):
                return self.nombre