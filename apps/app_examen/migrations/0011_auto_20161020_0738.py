# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0010_auto_20161020_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='alumno',
            field=models.ForeignKey(to='app_examen.Alumno', null=True),
        ),
        migrations.AddField(
            model_name='examen',
            name='materia',
            field=models.ForeignKey(to='app_examen.Materia', null=True),
        ),
        migrations.AddField(
            model_name='examen',
            name='profesor',
            field=models.ForeignKey(to='app_examen.Profesor', null=True),
        ),
        migrations.AddField(
            model_name='examen',
            name='unidad',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
    ]
