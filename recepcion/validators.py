from django.core.exceptions import ValidationError
from django.utils.timezone import now

# def validar_par(value):
#     if value % 2 != 0:
#         raise ValidationError(f'{value} no es un número par.')

def validar_formato_hojaruta(value):
    if not value.startswith('HR '):
        raise ValidationError(f'{value} no comienza con el prefijo "HR ".')
    
def validar_fecha_recepcion(value):
    if value > now():
        raise ValidationError(f'{value} es una fecha futura. La fecha de recepción no puede ser en el futuro.')
    
def validar_fecha_recepcion_hora(value):
    if value.hour > 16:
        raise ValidationError(f'{value} es una hora mayor a 16:00. La hora de recepción no puede ser posterior a las 16:00.')