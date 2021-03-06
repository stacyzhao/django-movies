# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 01:44
from __future__ import unicode_literals

from django.db import migrations
import csv
from ratings.models import Rating, Movie, Rater


def get_rating(apps, schema_editor):
    rating = apps.get_model("ratings", "Rating")
    with open('../ml-100k/u.data', 'r') as f:
        data = csv.reader(f, delimiter='\t')
        for row in data:
            rater = Rater.objects.get(id=row[0])
            movie = Movie.objects.get(id=row[1])

            rating = Rating(rater=rater, movie=movie, rating=row[2])
            rating.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20160507_0142'),
    ]

    operations = [
        migrations.RunPython(get_rating),
    ]
