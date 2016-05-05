from django.db import models
import datetime


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(default=datetime.date.today)

    # def __str__(self):
    #     return self.title, self.release_date


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    #
    # def __str__(self):
    #     return self.user_id, self.age


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()

    # def __str__(self):
    #     return self.user_id, self.movie_id, self.rating
