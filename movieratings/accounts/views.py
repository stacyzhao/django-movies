from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ratings.models import Movie, Rating, Rater


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def profile(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # movie = get_object_or_404(Movie, pk=id)
    # ratings = movie.rating_set.all()
    top_movies = Movie.objects.order_by('-avg_rating')[:20]
    if request.POST:
        print('POST', request.POST['movie'], request.POST['rating'])
    context = {
        'movies': Movie.objects.all(),
        'ratings': Rating.objects.all(),
        'top_movies': top_movies
    }
    return render(request, 'accounts/profile.html', context)
