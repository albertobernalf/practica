from django.contrib import admin

# Register your models here.

from sitios.models import Departamentos, Ciudades, Centros, SedesClinica, DependenciasTipo, Dependencias, DependenciasActual


class sedesClinicaAdmin(admin.ModelAdmin):


    list_display = ("id","departamentos","ciudades" , "nombre","direccion", "telefono", "contacto","fechaRegistro","usuarioRegistro")
    search_fields = ("id","departamentos","ciudades", "nombre","direccion", "telefono", "contacto","fechaRegistro","usuarioRegistro")


class departamentosAdmin(admin.ModelAdmin):

    list_display=("id","nombre")
    search_fields =("id","nombre")

class ciudadesAdmin(admin.ModelAdmin):

    list_display=("id","departamentos","nombre")

    search_fields =('id','departamentos_id__departamentos','nombre')

class centrosAdmin(admin.ModelAdmin):

        list_display = ("id","departamentos","ciudades" , "nombre","direccion", "telefono", "contacto","fechaRegistro","usuarioRegistro")
        search_fields = ("id","departamentos","ciudades" , "nombre","direccion", "telefono", "contacto","fechaRegistro","usuarioRegistro")



class dependenciasTipoAdmin(admin.ModelAdmin):


    list_display = ("id","nombre")
    search_fields = ("id","nombre")


class dependenciasAdmin(admin.ModelAdmin):


    list_display = ("id","sedesClinica", "dependenciasTipo", "servicios", "nombre", "descripcion","fechaRegistro","usuarioRegistro")
    search_fields = ("id","sedesClinica", "dependenciasTipo", "servicios", "nombre", "descripcion","fechaRegistro","usuarioRegistro")


class dependenciasActualAdmin(admin.ModelAdmin):


    list_display = ("id","dependencias", "tipoDoc",  "nombre", "descripcion","documento","consec","fechaRegistro","usuarioRegistro")
    search_fields = ("id","dependencias", "tipoDoc",  "nombre", "descripcion","documento","consec","fechaRegistro","usuarioRegistro")





admin.site.register(SedesClinica, sedesClinicaAdmin)
admin.site.register(Departamentos, departamentosAdmin)
admin.site.register(Ciudades, ciudadesAdmin)
admin.site.register(Centros, centrosAdmin)
admin.site.register(DependenciasTipo, dependenciasTipoAdmin)
admin.site.register(Dependencias, dependenciasAdmin)
admin.site.register(DependenciasActual, dependenciasActualAdmin)
