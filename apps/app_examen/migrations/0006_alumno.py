# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_examen', '0005_remove_profesor_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=64)),
                ('n_control', models.CharField(max_length=64)),
                ('categoria', models.CharField(default=b'alumno', max_length=64, null=True)),
                ('user_perfil', models.OneToOneField(related_name='profile_a', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
