from django.http import HttpResponse
from .models import Movie, Rating, Rater
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count
from django.template import loader


def index(request):
    avg_list = Rating.objects.annotate(avg_rating=Avg('movie_id')).order_by('-average_stars').order_by('-avg')
    template = loader.get_template('ratings/index.html')
    context = {
        'avg_list': avg_list,
    }
    return HttpResponse(template.render(context, request))


def get_movies(request):
    movie_list = Movie.objects.order_by('-avg_rating')[:20]
    # output = ', '.join([q.title for q in movie_list])
    # template = loader.get_template('ratings/movie.html')
    context = {'movie_list': movie_list}
    return render(request, 'ratings/movie.html', context)


def get_ratings(request):
    rating_list = Rating.objects.annotate(num_rating=Count('movie_id'))[:10]
    context = {'rating_list': rating_list}
    return render(request, 'ratings/rating.html', context)


def get_raters(request):
    rater_list = Rater.objects.order_by('id')
    # output = ', '.join([q.age for q in rater_list])
    # template = loader.get_template('ratings/rating.html')
    context = {
        'rater_list': rater_list,
        }
    return render(request, 'ratings/rating.html', context)

# def getsinglemovie(movie):
    # get movie object = movie
