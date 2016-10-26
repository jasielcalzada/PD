# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0009_auto_20161020_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='respuesta',
            name='corecta',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='examen',
            name='pregun',
            field=models.ForeignKey(to='app_examen.Preguntas'),
        ),
        migrations.AddField(
            model_name='examen',
            name='respue',
            field=models.ForeignKey(to='app_examen.Respuesta'),
        ),
    ]
