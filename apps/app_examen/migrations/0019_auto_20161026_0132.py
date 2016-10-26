# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0018_auto_20161024_0640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuesta',
            old_name='pregunta',
            new_name='pregun',
        ),
    ]
