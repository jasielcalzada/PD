# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='categoria',
            field=models.CharField(default=b'profesor', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='user_perfil',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
