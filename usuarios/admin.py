from django.contrib import admin

# Register your models here.

from usuarios.models import TiposDocumento, TiposUsuario, Usuarios


class tiposDocumentoAdmin(admin.ModelAdmin):

    list_display=("id","abreviatura","nombre")
    search_fields =("id","abreviatura","nombre")

class tiposUsuarioAdmin(admin.ModelAdmin):

        list_display = ("id", "nombre")
        search_fields = ("id", "nombre")


class usuariosAdmin(admin.ModelAdmin):

    list_display = ("id","id_tipo_doc","documento","nombre","genero")
    search_fields = ("id","tid_ipo_doc","documento","nombre","genero")


admin.site.register(TiposDocumento, tiposDocumentoAdmin)
admin.site.register(TiposUsuario, tiposUsuarioAdmin)
admin.site.register(Usuarios, usuariosAdmin)

