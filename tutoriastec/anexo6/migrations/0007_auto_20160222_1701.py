# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo6', '0006_auto_20160217_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosgenerales',
            name='becado_institucion',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='datosgenerales',
            name='numero_hijos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='estado_civil',
            field=models.CharField(choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('otro', 'Otro')], default='soltero', max_length=50),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='numero_control',
            field=models.CharField(max_length=50),
        ),
    ]
