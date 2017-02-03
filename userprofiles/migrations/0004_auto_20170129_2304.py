# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-29 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0019_auto_20170129_2304'),
        ('userprofiles', '0003_auto_20170119_0430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='team',
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='players', to='games_information.Team', verbose_name='Equipo en el que juega'),
        ),
    ]