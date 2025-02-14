# Generated by Django 5.1.4 on 2024-12-08 18:13

import django.utils.timezone
import recepcion.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hojaruta',
            name='codigo_hojaruta',
            field=models.CharField(max_length=20, unique=True, validators=[recepcion.validators.validar_formato_hojaruta]),
        ),
        migrations.AlterField(
            model_name='hojaruta',
            name='fecha_recepcion',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[recepcion.validators.validar_fecha_recepcion, recepcion.validators.validar_fecha_recepcion_hora]),
        ),
        migrations.AlterField(
            model_name='remitente',
            name='domicilio',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='remitente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='remitente',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
