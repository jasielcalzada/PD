# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0008_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='preguntas',
            name='respuesta',
            field=models.ForeignKey(blank=True, to='app_examen.Respuesta', null=True),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='opcion1',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='opcion2',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='opcion3',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='opcion',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
