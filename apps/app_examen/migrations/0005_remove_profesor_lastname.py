# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0004_materia_profesor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='lastname',
        ),
    ]
