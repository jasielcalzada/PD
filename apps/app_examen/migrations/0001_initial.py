# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('user_perfil', models.OneToOneField(related_name='profesores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
