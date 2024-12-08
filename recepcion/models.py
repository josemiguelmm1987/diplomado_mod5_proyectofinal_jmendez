from django.db import models
from .validators import validar_formato_hojaruta, validar_fecha_recepcion, validar_fecha_recepcion_hora
from django.utils.timezone import now

# Create your models here.
class Procedencia(models.Model):
    nombre = models.CharField(max_length=2500, unique=True)
    def __str__(self):
        return self.nombre

class Cargo(models.TextChoices):
    NO_ESPECIFICADO = 'NOE', 'No Especificado'
    CONCEJAL_A = 'CJAL', 'Concejal/a'
    ALCALDE_SA = 'ALC', 'Alcalde/sa'
    PRESIDENTE = 'PRES', 'Presidente'
    VICEPRESIDENTE = 'VICE', 'Vicepresidente'
    SECRETARIO_A = 'SEC', 'Secretario/a'
    REPRESENTANTE = 'REPRES', 'Representante'

class Remitente(models.Model):
    nombre = models.CharField(max_length=2500, unique=True)
    def __str__(self):
        return self.nombre
    
    cargo = models.CharField(
        max_length=100,
        choices=Cargo.choices,
        default=Cargo.NO_ESPECIFICADO
    )
    procedencia = models.ForeignKey(Procedencia, on_delete=models.CASCADE)
    domicilio = models.CharField(max_length=2500, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

class TipoDocumento(models.TextChoices):
    NO_ESPECIFICADO = 'NOE', 'No Especificado'
    CITE = 'CITE', 'CITE'
    INFORME = 'INF', 'Informe'
    MEMORIAL = 'MEMORIAL', 'MEMORIAL'
    PROYECTO_MINUTA_COMUNICACION = 'PMC', 'Proyecto de Minuta de Comunicación'
    PROYECTO_PETICION_INFORME_ESCRITO = 'PPIE', 'Proyecto de Petición de Informe Escrito'
    PROYECTO_PETICION_INFORME_ORAL = 'PPIO', 'Proyecto de Petición de Informe Oral'
class Documento(models.Model):
    codigo_documento = models.CharField(max_length=250)
    def __str__(self):
        return self.codigo_documento
    
    tipo_documento = models.CharField(
        max_length=100,
        choices=TipoDocumento.choices,
        default=TipoDocumento.NO_ESPECIFICADO
    )
class HojaRuta(models.Model):
    codigo_hojaruta = models.CharField(max_length=20, unique=True, validators=[validar_formato_hojaruta])
    def __str__(self):
        return self.codigo_hojaruta
    
    remitente = models.ForeignKey(Remitente, on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    referencia = models.TextField()
    # fecha_recepcion = models.DateTimeField(auto_now=True, validators=[validar_fecha_recepcion, validar_fecha_recepcion_hora])
    fecha_recepcion = models.DateTimeField(default=now, validators=[validar_fecha_recepcion, validar_fecha_recepcion_hora])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)