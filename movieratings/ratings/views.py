from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, Rating, Rater
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login


def index(request):
    # movie = Movie.objects.get(pk=movie_id)
    movies = Movie.objects.order_by('-avg_rating')[:20]
    return render(request, 'ratings/index.html', {'movies': movies})


def top_movies(request):
    movies = Movie.objects.order_by('-avg_rating')[:20]
    return render(request, 'ratings/top_movies.html', {'movies': movies})


def get_movies(request, movie_id):
    # movie = Movie.get_object_or_404(Movie, pk=movie_id)
    movie = get_object_or_404(Movie, pk=movie_id)
    # movie = Movie.objects.get(pk=movie_id)
    # output = ', '.join([q.title for q in movie_list])
    # template = loader.get_template('ratings/movie.html')
    ratings = movie.rating_set.all()
    context = {
        'movie': movie,
        'ratings': ratings,
    }
    return render(request, 'ratings/movie.html', context)


# def get_ratings(request):
#     rating_list = Rating.objects.annotate(num_rating=Count('movie_id'))[:10]
#     context = {'rating_list': rating_list}
#     return render(request, 'ratings/rating.html', context)


def get_raters(request, rater_id):
    rater = get_object_or_404(Rater, pk=rater_id)
    ratings = rater.rating_set.all()
    # rater_list = Rater.objects.order_by('id')
    # output = ', '.join([q.age for q in rater_list])
    # template = loader.get_template('ratings/rating.html')
    context = {
        'rater': rater,
        'ratings': ratings,
        }
    return render(request, 'ratings/rater.html', context)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print("success")
        else:
            return HttpResponseRedirect('/accounts/invalid')
    else:
        print("The username and password were incorrect.")
