# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-03 00:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0002_auto_20170427_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(error_messages={'unique': 'A team with that name already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[\\d\\/. ()\\-+]+$', 'Enter a valid name team. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='name'),
        ),
    ]