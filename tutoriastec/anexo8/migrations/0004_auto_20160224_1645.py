# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo8', '0003_auto_20160224_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='areaintegracion',
            name='actitud_con_adre',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='actitud_con_padre',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='relacion_con_madre',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='relacion_con_padre',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AddField(
            model_name='datoshermanos',
            name='actitud_con_hermano',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AddField(
            model_name='datoshermanos',
            name='relacion_con_hermano',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AlterField(
            model_name='areaintegracion',
            name='actitud_con_familia',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AlterField(
            model_name='areaintegracion',
            name='dificultades_fam',
            field=models.CharField(choices=[('si', 'Si'), ('no', 'No')], default='2', max_length=50),
        ),
        migrations.AlterField(
            model_name='areaintegracion',
            name='relacion_familia',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AlterField(
            model_name='estadopsicofisiologicos',
            name='mop_hinchados',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AlterField(
            model_name='estadopsicofisiologicos',
            name='observaciones_higiene',
            field=models.TextField(),
        ),
    ]
