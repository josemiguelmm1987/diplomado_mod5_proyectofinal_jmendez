# Generated by Django 5.1.4 on 2024-12-08 02:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_documento', models.CharField(max_length=250)),
                ('tipo_documento', models.CharField(choices=[('NOE', 'No Especificado'), ('CITE', 'CITE'), ('INF', 'Informe'), ('MEMORIAL', 'MEMORIAL'), ('PMC', 'Proyecto de Minuta de Comunicación'), ('PPIE', 'Proyecto de Petición de Informe Escrito'), ('PPIO', 'Proyecto de Petición de Informe Oral')], default='NOE', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Procedencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=2500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remitente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=2500, unique=True)),
                ('cargo', models.CharField(choices=[('NOE', 'No Especificado'), ('CJAL', 'Concejal/a'), ('ALC', 'Alcalde/sa'), ('PRES', 'Presidente'), ('VICE', 'Vicepresidente'), ('SEC', 'Secretario/a'), ('REPRES', 'Representante')], default='NOE', max_length=100)),
                ('domicilio', models.CharField(max_length=2500)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('procedencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.procedencia')),
            ],
        ),
        migrations.CreateModel(
            name='HojaRuta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_hojaruta', models.CharField(max_length=20, unique=True)),
                ('referencia', models.TextField()),
                ('fecha_recepcion', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.documento')),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.remitente')),
            ],
        ),
    ]
