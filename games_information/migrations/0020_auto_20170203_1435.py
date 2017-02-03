# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-03 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0019_auto_20170129_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='branch',
            field=models.CharField(blank=True, choices=[('', ''), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default=False, max_length=12, verbose_name='Rama'),
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(blank=True, choices=[('', ''), ('Empresa', 'Empresa'), ('Barrio', 'Barrio'), ('Universidad', 'Universidad'), ('Colegio', 'Colegio'), ('Infantil', 'Infantil'), ('Master', 'Master'), ('Sin Categoría', 'Sin Categoría')], default='Sin Categoría', max_length=40, verbose_name='Categoría'),
        ),
    ]