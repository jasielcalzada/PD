# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0013_remove_preguntas_fecha_publicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='preguntas',
            name='opcion1',
            field=models.BooleanField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='opcion2',
            field=models.BooleanField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='opcion3',
            field=models.BooleanField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='opcion4',
            field=models.BooleanField(default=False, max_length=200),
        ),
    ]
