# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-03 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0006_auto_20170503_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
