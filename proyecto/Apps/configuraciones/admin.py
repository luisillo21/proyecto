from django.contrib import admin
from proyecto.Apps.configuraciones.models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Persona)
admin.site.register(Permisos)
admin.site.register(Menu)
admin.site.register(ConfUsuario_rol)
admin.site.register(Rol)