from django.db import models


class Rating(models.Model):
    user_id = models.ForeignKey('Rater', on_delete=models.CASCADE)
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user_id, self.movie_id, self.rating


class Rater(models.Model):
    user_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.user_id, self.age


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()

    def __str__(self):
        return self.title, self.release_date
