# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0002_auto_20161113_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]