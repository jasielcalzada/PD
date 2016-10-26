# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0014_auto_20161023_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='opcion1',
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='opcion2',
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='opcion3',
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='opcion4',
        ),
    ]
