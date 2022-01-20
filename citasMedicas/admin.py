from django.contrib import admin

# Register your models here.

from clinico.models import Medicos, Especialidades
from citasMedicas.models import ConsTipo, Agenda, Cons, ConsAgenda, AgendaMedica, CitasEstados , CitasMedicas,ControlCitas


class agendaAdmin(admin.ModelAdmin):

        list_display = ("id", "nombre","fecha_desde","fecha_hasta")
        search_fields = ("id", "nombre","fecha_desde","fecha_hasta")

class consTipoAdmin(admin.ModelAdmin):

    list_display = ("id", "nombre")
    search_fields = ("id", "nombre")

class consAdmin(admin.ModelAdmin):

    list_display = ("id","id_ConsTipo" , "nombre","id_depto","id_ciudad","direccion","telefono")
    search_fields = ("id","id_ConsTipo" , "nombre","id_depto","id_ciudad","direccion","telefono")

class consAgendaAdmin(admin.ModelAdmin):
    list_display = ("id","id_Agenda","id_Cons","lunes_desde","lunes_hasta")
    search_fields = ("id","id_Agenda","id_Cons","lunes_desde","lunes_hasta")


class agendaMedicaAdmin(admin.ModelAdmin):

    list_display = ("id","id_ConsAgenda","id_Medico","lunes_desde","lunes_hasta")
    search_fields = ("id","id_ConsAgenda","id_Medico","lunes_desde","lunes_hasta")


class citasEstadosAdmin(admin.ModelAdmin):

        list_display = ("id", "nombre")
        search_fields = ("id", "nombre")

class controlCitasAdmin(admin.ModelAdmin):
            list_display = ("id", "id_cita","fecha","estado")
            search_fields = ("id", "id_cita","fecha","estado")

class citasMedicasAdmin(admin.ModelAdmin):
            list_display = ("id", "numcita", "id_AgendaMedica", "id_documento", "fecha_desde", "hora_desde", "fecha_hasta",
                "hora_hasta")
            search_fields = ("id", "nombre")




admin.site.register(Agenda, agendaAdmin)
admin.site.register(ConsTipo, consTipoAdmin)
admin.site.register(Cons, consAdmin)
admin.site.register(ConsAgenda, consAgendaAdmin)
admin.site.register(AgendaMedica, agendaMedicaAdmin)
admin.site.register(CitasEstados, citasEstadosAdmin)

admin.site.register(CitasMedicas, citasMedicasAdmin)
admin.site.register(ControlCitas, controlCitasAdmin)