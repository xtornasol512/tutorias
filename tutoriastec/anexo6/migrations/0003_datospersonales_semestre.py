# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-14 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo6', '0002_remove_datospersonales_semestre'),
    ]

    operations = [
        migrations.AddField(
            model_name='datospersonales',
            name='semestre',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='1', max_length=50),
        ),
    ]
