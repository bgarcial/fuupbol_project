# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-19 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0011_remove_match_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='check_match_away_team',
            field=models.BooleanField(default=False),
        ),
    ]