# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoyageCalc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='comission',
            field=models.FloatField(default=0.0),
        ),
    ]
