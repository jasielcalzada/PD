# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0011_auto_20161020_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='respuesta',
            field=models.ForeignKey(to='app_examen.Respuesta', null=True),
        ),
    ]
