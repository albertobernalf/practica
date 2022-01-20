from django.contrib import admin

# Register your models here.

from planta.models import TiposPlanta, Planta, PerfilesPlanta



class tiposPlantaAdmin(admin.ModelAdmin):

    list_display=("id","nombre")
    search_fields =("id","nombre")

class perfilesPlantaAdmin(admin.ModelAdmin):

        list_display = ("id", "id_tipo_doc", "documento", "id_perfilPlanta")
        search_fields =  ("id", "id_tipo_doc", "documento", "id_perfilPlanta")


class plantaAdmin(admin.ModelAdmin):

    list_display = ("id","id_tipo_doc","documento","nombre","genero")
    search_fields = ("id","tid_ipo_doc","documento","nombre","genero")


admin.site.register(TiposPlanta, tiposPlantaAdmin)
admin.site.register(PerfilesPlanta, perfilesPlantaAdmin)
admin.site.register(Planta, plantaAdmin)



