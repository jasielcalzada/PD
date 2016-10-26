# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0003_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
