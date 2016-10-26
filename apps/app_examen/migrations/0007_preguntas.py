# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0006_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(auto_now=True, verbose_name=b'fecha de publicacion')),
                ('dificultad', models.CharField(max_length=64, choices=[(b'Facil', b'Facil'), (b'Intermedio', b'Intermedio'), (b'Dificil', b'Dificil')])),
                ('valor', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]
