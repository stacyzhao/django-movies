# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20160507_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
