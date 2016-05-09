from django.db import models
from django.contrib.auth.models import User
import datetime


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(default=datetime.date.today)
    avg_rating = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.title, self.release_date)


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=50)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Age: {}, Gender: {}".format(self.age, self.gender)


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return "{}, {}, {}".format(self.rater, self.movie, self.rating)
