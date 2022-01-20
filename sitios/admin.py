from django.contrib import admin

# Register your models here.

from sitios.models import Departamentos, Ciudades, Centros

class departamentosAdmin(admin.ModelAdmin):

    list_display=("id","nombre")
    search_fields =("id","nombre")

class ciudadesAdmin(admin.ModelAdmin):

    list_display=("id","id_departamento","nombre")
    search_fields =("id","id_departamento","nombre")

class centrosAdmin(admin.ModelAdmin):

        list_display = ("id", "nombre","direccion","telefono","contacto")
        search_fields = ("id", "nombre","direccion","telefono","contacto")



admin.site.register(Departamentos, departamentosAdmin)
admin.site.register(Ciudades, ciudadesAdmin)
admin.site.register(Centros, centrosAdmin)