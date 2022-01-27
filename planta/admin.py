from django.contrib import admin

# Register your models here.

from planta.models import TiposPlanta, Planta, PerfilesPlanta



class tiposPlantaAdmin(admin.ModelAdmin):

    list_display=("id","nombre")
    search_fields =("id","nombre")

class perfilesPlantaAdmin(admin.ModelAdmin):

        list_display = ("id", "sedesClinica", "planta", "tiposPlanta","fechaRegistro","usuarioRegistro")
        search_fields =  ("id", "sedesClinica", "planta", "tiposPlanta","fechaRegistro","usuarioRegistro")


class plantaAdmin(admin.ModelAdmin):

    list_display = ("id","sedesClinica","tipoDoc","documento","nombre","genero","direccion","telefono","fechaRegistro","usuarioRegistro")
    search_fields = ("id","sedesClinica","tipoDoc","documento","nombre","genero","direccion","telefono","fechaRegistro","usuarioRegistro")


admin.site.register(TiposPlanta, tiposPlantaAdmin)
admin.site.register(PerfilesPlanta, perfilesPlantaAdmin)
admin.site.register(Planta, plantaAdmin)



