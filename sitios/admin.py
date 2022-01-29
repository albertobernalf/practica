from django.contrib import admin

# Register your models here.

from sitios.models import Departamentos, Ciudades, Centros, SedesClinica, DependenciasTipo, Dependencias, DependenciasActual

@admin.register(SedesClinica)
class sedesClinicaAdmin(admin.ModelAdmin):


    list_display = ("id","departamentos","ciudades" , "nombre","direccion", "telefono", "contacto","fechaRegistro")
    search_fields = ("id","departamentos","ciudades", "nombre","direccion", "telefono", "contacto","fechaRegistro")
    #Filtrar
    list_filter =('nombre', 'ciudades')




class CiudadesInline(admin.StackedInline):
        model =Ciudades
        fields = ('nombre',)
        Extra = 0
        # Filtrar
        list_filter = ('nombre',)


class DepartamentosAdmin(admin.ModelAdmin):

    Inlines = [CiudadesInline]
    list_display=("id","nombre")

    search_fields =("id","nombre")
    # Filtrar
    list_filter = ('nombre',)

admin.site.register(Departamentos, DepartamentosAdmin)
admin.site.register(Ciudades)


#@admin.register(Ciudades)
#class ciudadesAdmin(admin.ModelAdmin):

#    list_display=("id","departamentos","nombre")

#    search_fields =('id','departamentos','nombre')
    # Filtrar
#    list_filter = ('nombre','departamentos')

@admin.register(Centros)
class centrosAdmin(admin.ModelAdmin):

        list_display = ("id","departamentos","ciudades" , "nombre","direccion", "telefono", "contacto","fechaRegistro")
        search_fields = ("id","departamentos","ciudades" , "nombre","direccion", "telefono", "contacto","fechaRegistro")
        # Filtrar
        list_filter = ('nombre','departamentos','ciudades','contacto')







@admin.register(DependenciasTipo)
class dependenciasTipoAdmin(admin.ModelAdmin):


    list_display = ("id","nombre")
    search_fields = ("id","nombre")
    # Filtrar
    list_filter = ('nombre',)

@admin.register(Dependencias)
class dependenciasAdmin(admin.ModelAdmin):


    list_display = ("id","sedesClinica", "dependenciasTipo", "servicios", "nombre", "descripcion")
    search_fields = ("id","sedesClinica", "dependenciasTipo", "servicios", "nombre", "descripcion")
    # Filtrar
    list_filter = ('nombre', 'dependenciasTipo','servicios','descripcion')


@admin.register(DependenciasActual)
class dependenciasActualAdmin(admin.ModelAdmin):


    list_display = ("id","dependencias", "tipoDoc",  "nombre", "descripcion","documento","consec","fechaRegistro")
    search_fields = ("id","dependencias", "tipoDoc",  "nombre", "descripcion","documento","consec","fechaRegistro")


admin.site.site_header = 'Clinica Vulnerable'
admin.site.index_title = 'Panel de control '
admin.site.site_title = 'Administracion'



