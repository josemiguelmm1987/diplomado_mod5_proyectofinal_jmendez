from django.contrib import admin
from .models import Documento, HojaRuta, Procedencia, Remitente

# Register your models here.
admin.site.register(Documento)
admin.site.register(Procedencia)
admin.site.register(Remitente)

class HojaRutaAdmin(admin.ModelAdmin):
    list_display = ('codigo_hojaruta', 'documento', 'remitente', 'referencia', 'fecha_recepcion')
    ordering = ('documento', )
    search_fields = ('referencia', )
    list_filter = ('remitente', )
admin.site.register(HojaRuta, HojaRutaAdmin)