# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0016_preguntas_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='respuesta',
        ),
    ]
