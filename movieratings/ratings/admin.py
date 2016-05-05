from django.contrib import admin

from .models import Rating, Rater, Movie

admin.site.register(Rating)
admin.site.register(Rater)
admin.site.register(Movie)
