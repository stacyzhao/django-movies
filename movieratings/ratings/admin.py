from django.contrib import admin
from .models import Rating, Rater, Movie


class RaterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Profile', {'fields': ['age', 'gender', 'occupation']}),
    ]
admin.site.register(Rater, RaterAdmin)


class RatingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Rating', {'fields': ['rating', 'review']}),
    ]
admin.site.register(Rating, RatingAdmin)


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Movie', {'fields': ['title', 'release_date']}),
    ]
admin.site.register(Movie, MovieAdmin)
