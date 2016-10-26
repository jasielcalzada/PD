# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0017_remove_preguntas_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='opcion1',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='opcion2',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='opcion3',
        ),
        migrations.AddField(
            model_name='respuesta',
            name='pregunta',
            field=models.ForeignKey(to='app_examen.Preguntas', null=True),
        ),
    ]
