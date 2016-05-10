from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, Rating, Rater
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RatingForm

def index(request):
    # movie = Movie.objects.get(pk=movie_id)
    movies = Movie.objects.order_by('-avg_rating')[:20]
    return render(request, 'ratings/index.html', {'movies': movies})


def top_movies(request):
    movies = Movie.objects.order_by('-avg_rating')[:20]
    return render(request, 'ratings/top_movies.html', {'movies': movies})


def get_movies(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = movie.rating_set.all()
    rating = Rating.objects.filter(movie_id=movie_id, rater_id=request.user.rater.id).first()
    form = RatingForm()
    # 'SELECT * FROM ratings where movie_id = "rater_id";'
    context = {
        'movie': movie,
        'ratings': ratings,
        'rating': rating,
        'form': form,
    }
    return render(request, 'ratings/movie.html', context)
    # movie = Movie.get_object_or_404(Movie, pk=movie_id)
    # movie = Movie.objects.get(pk=movie_id)
    # output = ', '.join([q.title for q in movie_list])
    # template = loader.get_template('ratings/movie.html')


# def get_ratings(request):
#     rating_list = Rating.objects.annotate(num_rating=Count('movie_id'))[:10]
#     context = {'rating_list': rating_list}
#     return render(request, 'ratings/rating.html', context)

# def get_rating(request):
#     movie = get_object_or_404(Movie, pk=movie_id)


def get_raters(request, rater_id):
    rater = get_object_or_404(Rater, pk=rater_id)
    ratings = rater.rating_set.all()
    context = {
        'rater': rater,
        'ratings': ratings,
        }
    return render(request, 'ratings/rater.html', context)

    # rater_list = Rater.objects.order_by('id')
    # output = ', '.join([q.age for q in rater_list])
    # template = loader.get_template('ratings/rating.html')

# def user_login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return HttpResponseRedirect('/ratings/top_movies/')
#         else:
#             return HttpResponseRedirect("account disabled")
#     else:
#         return HttpResponse("invalid username or password")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/logout/')


def add_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            rating_obj = Rating(rater=request.user.rater, movie=movie, rating=rating)
            rating_obj.save()
            return HttpResponseRedirect('/ratings/movie/' + movie_id)
    else:
        form = RatingForm()

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'ratings/add_rating.html', context)
