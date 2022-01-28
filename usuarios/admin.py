from django.contrib import admin

# Register your models here.

from usuarios.models import TiposDocumento, TiposUsuario, Usuarios


class tiposDocumentoAdmin(admin.ModelAdmin):

    list_display=("id","abreviatura","nombre","fechaRegistro")
    search_fields =("id","abreviatura","nombre","fechaRegistro")


class tiposUsuarioAdmin(admin.ModelAdmin):

        list_display = ("id", "nombre","fechaRegistro")
        search_fields = ("id", "nombre","fechaRegistro")


class usuariosAdmin(admin.ModelAdmin):

    list_display = ("id","tipoDoc","documento","nombre","genero","centrosC","tiposUsuario","direccion","telefono","contacto")
    search_fields =("id","tipoDoc","documento","nombre","genero","centrosC","tiposUsuario","direccion","telefono","contacto")


admin.site.register(TiposDocumento, tiposDocumentoAdmin)
admin.site.register(TiposUsuario, tiposUsuarioAdmin)
admin.site.register(Usuarios, usuariosAdmin)

