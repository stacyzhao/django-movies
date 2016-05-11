from django import forms
from .models import Rating


class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    review = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Rating
        fields = ['rating', 'review']

# Make sure new ratings are timestamped correctly.
# date time field in models
# auto_now_add=true field: created_at




# Add a personal page for each user that only they can see. It should have all their ratings and allow them to edit or delete those ratings.

# Add a public page for each user that has all their ratings and their user info.
# Movies should have genres, and each genre should have a page where you can see the top rated movies for that genre.
# Have a page both for showing movies with the most ratings and movies with the highest ratings.

# General flow
# project url
# app url - give it a name and name space
# define view function
# return fake httpresponse to check if url works
# model queries (views.py) define functions or render template
