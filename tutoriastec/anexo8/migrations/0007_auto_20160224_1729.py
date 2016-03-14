# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo8', '0006_areaintegracion_actitud_con_madre'),
    ]

    operations = [
        migrations.AddField(
            model_name='areaintegracion',
            name='influido_estudiar',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='ocupa_educacion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='otro_inf_familiar',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='pareja',
            field=models.CharField(choices=[('si', 'Si'), ('no', 'No')], default='no', max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='relacion_companeros_porque',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='relacion_con_amigos',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='relacion_con_companeros',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='relacion_pareja',
            field=models.CharField(choices=[('1', 'Muy buena'), ('2', 'Buena'), ('3', 'Regular'), ('4', 'Mala'), ('5', 'Muy mala')], default='2', max_length=50),
        ),
        migrations.AddField(
            model_name='areaintegracion',
            name='sientes_ligado_por',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='areaintegracion',
            name='dificultades_fam',
            field=models.CharField(choices=[('si', 'Si'), ('no', 'No')], default='no', max_length=50),
        ),
    ]
