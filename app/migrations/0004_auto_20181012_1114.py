# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 11:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181012_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='average',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
