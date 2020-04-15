from django.contrib import admin
from .models import *
# Register your models here.

class PaisAdmin(admin.ModelAdmin):
    pass

class ProvinciaAdmin(admin.ModelAdmin):
    pass

class CiudadAdmin(admin.ModelAdmin):
    pass

class MonedaAdmin(admin.ModelAdmin):
    pass

class TipodocumentoAdmin(admin.ModelAdmin):
    pass

class EmpresaAdmin(admin.ModelAdmin):
    pass

class PaisAdmin(admin.ModelAdmin):
    pass

class OficinaAdmin(admin.ModelAdmin):
    pass

class EmpleadoAdmin(admin.ModelAdmin):
    pass

class TipoausenciaAdmin(admin.ModelAdmin):
    pass

class AusenciaAdmin(admin.ModelAdmin):
    pass

class EquipoAdmin(admin.ModelAdmin):

    pass

class EventoAdmin(admin.ModelAdmin):
    pass

class TareaAdmin(admin.ModelAdmin):
    pass

class DiafestivoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Ciudad, CiudadAdmin)

admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Tipodocumento, TipodocumentoAdmin)
admin.site.register(TipoAusencia, TipoausenciaAdmin)

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Oficina, OficinaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)

admin.site.register(Ausencia, AusenciaAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Diafestivo, DiafestivoAdmin)

