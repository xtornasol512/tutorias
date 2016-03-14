# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo13', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta1',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='En una reunio dficil, con con un ambiente tenso,soy capaz de hablar con confianza'),
        ),
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta2',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='Si no estoy segura de una cosa, puedo pedir ayuda facilmente.'),
        ),
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta3',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='Si alguna persona es injusta y agresiva, puedo controlar la situacion con confianza.'),
        ),
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta4',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='si alguna persona se muestra ironica conmigo o con otras, puedo responder sin agresividad'),
        ),
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta5',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='Si creo que se esta abusando de mi, soy capaz de denunciarlo sin alterarme.'),
        ),
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta6',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='Si alguna persona me pide permiso para hacer algo que no me gusta, por ejemplo, fumar, puedo decirle que no sin sentirme culpable'),
        ),
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta7',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='Si alguna persona pide mi opinion sobre alguna cosa me siento bien dandosela, aunque no concuerde con la de los demas'),
        ),
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta8',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='Puedo conectar facil y efectivamente con personas que considero importantes'),
        ),
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta9',
            field=models.CharField(choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], max_length=50, verbose_name='Cuando encuentro defectos en una tienda o restaurante, soy capaz de exponerlos sin atacar a las otras personas y sin sentirme mal'),
        ),
    ]
