# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-11 13:05
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAutoestima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pregunta1', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'A la hora de tomar decisiones en tu vida, como proponer cosas nuevas en el trabajo, iniciar alguna actividad de ocio, o elegir un color nuevo para pintar tu casa, \xc2\xbfsueles buscar la aprobaci\xc3\xb3n o el apoyo de las personas que te rodean?')),
                ('pregunta2', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'Imagina que est\xc3\xa1s en una reuni\xc3\xb3n social o familiar importante; adviertes que 110 vas vestido para la ocasi\xc3\xb3n y que desentonas con los dem\xc3\xa1s, \xc2\xbfc\xc3\xb3mo te comportas?')),
                ('pregunta3', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'Tienes muchas ganas de irte a comprar ropa y le pides a alg\xc3\xban amigo que te acompa\xc3\xb1e. Esta persona es m\xc3\xa1s alta y m\xc3\xa1s atractiva que t\xc3\xba, y todo lo que se prueba le queda mucho mejor que a ti.')),
                ('pregunta4', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'Un d\xc3\xada conoces a alguien nuevo y muy interesante, est\xc3\xa1is charlando animadamente y llega el momento de hablar de ti, \xc2\xbfcu\xc3\xa1l de las siguientes opciones mejor se ajusta a lo que cuentas?')),
                ('pregunta5', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'En tu lugar de trabajo o de estudios, se est\xc3\xa1 explicando algo que es completamente nuevo para ti. Llega un momento en que te das cuenta que no has entendido casi nada \xc2\xbfqu\xc3\xa9 haces?')),
                ('pregunta6', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'Tener un trabajo bien remunerado y que nos guste es algo dif\xc3\xadcil de conseguir, si tuvieras que valorar tu empleo o tu situaci\xc3\xb3n laboral, \xc2\xbfc\xc3\xb3mo la definir\xc3\xadas?')),
                ('pregunta7', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'Has tenido un d\xc3\xada duro, has trabajado con m\xc3\xa1s ah\xc3\xadnco para finalizar una tarea en la oficina, has hecho todas las gestiones que ten\xc3\xadas pendientes, has resuelto un par de problemas dom\xc3\xa9sticos y encima le has hecho un favor a un amigo. \xc2\xbfQu\xc3\xa9 haces al llegar a casa?')),
                ('pregunta8', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'En tu trabajo est\xc3\xa1n buscando a una persona que represente a la empresa en un concurso del ramo. Piden una persona que cumpla unos requisitos, entre ellos, explicar bien vuestro trabajo y que haga una demostraci\xc3\xb3n pr\xc3\xa1ctica del mismo.')),
                ('pregunta9', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'\xc2\xbfCon cu\xc3\xa1l de las siguientes frases sobre la buena fortuna est\xc3\xa1s m\xc3\xa1s de acuerdo?')),
                ('pregunta10', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('b', 'D')], max_length=2, verbose_name=b'En una fiesta en La que no conoces a nadie excepto a Los anfitriones, te presentan a un grupo de personas de aspecto interesante. \xc2\xbfCu\xc3\xa1l es tu actitud?')),
                ('diagnostico', models.CharField(blank=True, choices=[('1', 'Tienes un nivel algo bajo de autoestima.'), ('2', 'Tu nivel de autoestima es suficiente.'), ('3', 'Tu nivel de autoestima es muy bueno.'), ('4', 'Tienes un alto nivel de autoestima y mucha confianza y seguridad en ti mismo.')], max_length=2)),
                ('comentarios', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]