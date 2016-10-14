# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-12 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo6', '0008_remove_datospersonales_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosgenerales',
            name='becado_institucion',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='becado_lugar',
            field=models.CharField(blank=True, choices=[('federal', 'Gobierno Federal'), ('estatal', 'Gobierno Estatal'), ('bachillerato', 'Esfuerzo de Bachillerato')], default='federal', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='celular',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='con_quien_vives',
            field=models.CharField(choices=[('familia', 'Familia'), ('familia_cercana', 'Familia Cercana'), ('estudiantes', 'Estudiantes'), ('solo', 'Solo'), ('otros', 'Otros')], default='familia', max_length=50),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='escolaridad_madre',
            field=models.CharField(blank=True, choices=[('primaria', 'Primaria'), ('secundaria', 'Secundaria'), ('preparatoria', 'Preparatoria'), ('tecnico', 'T\xe9cnico'), ('lic', 'Licenciatura'), ('posgrado ', 'Posgrado'), ('sinestudio', 'Sin estudio')], default='sinestudio', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='escolaridad_padre',
            field=models.CharField(blank=True, choices=[('primaria', 'Primaria'), ('secundaria', 'Secundaria'), ('preparatoria', 'Preparatoria'), ('tecnico', 'T\xe9cnico'), ('lic', 'Licenciatura'), ('posgrado ', 'Posgrado'), ('sinestudio', 'Sin estudio')], default='sinestudio', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='nom_trabajo_madre',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='nom_trabajo_padre',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='numero_hijos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='telefono',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='trabajas_donde',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]