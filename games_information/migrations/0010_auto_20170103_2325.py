# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0009_auto_20170103_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='enterprise_name',
            field=models.CharField(default=1, max_length=150, verbose_name='Nombre de la empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='school_name',
            field=models.CharField(default=1, max_length=150, verbose_name='Nombre del colegio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='town_name',
            field=models.CharField(default=1, max_length=150, verbose_name='Nombre del barrio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='university_name',
            field=models.CharField(default=1, max_length=150, verbose_name='Nombre de la Universidad'),
            preserve_default=False,
        ),
    ]
