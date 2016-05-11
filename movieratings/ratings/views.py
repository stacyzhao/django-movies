from django.http import HttpResponseRedirect
from .models import Movie, Rating, Rater
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from .forms import RatingForm
from django.db.models import Avg, Count
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'ratings/index.html'
    context_object_name = 'movies'

    def get_queryset(self):
        count = Movie.objects.annotate(count=Count('rating')).filter(count__gt=100)
        return count.order_by('-avg_rating')[:20]


# class MovieView(generic.DetailView):
#     template_name = 'ratings/movie.html'
#     context_object_name = ['movies', 'ratings', 'rating', 'form']
#
#     def get_movies(self, **kwargs):
#         if request.user.is_authenticated():
#             rating = Rating.objects.filter(movie_id=movie_id, rater_id=request.user.rater.id).first()
#             form = RatingForm()
#         else:
#             rating = False
#             form = False
#         return rating, form

def get_movies(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = movie.rating_set.all()
    if request.user.is_authenticated():
        rating = Rating.objects.filter(movie_id=movie_id,
                                       rater_id=request.user.rater.id).first()
        form = RatingForm()
    else:
        rating = False
        form = False
    context = {
        'movie': movie,
        'ratings': ratings,
        'rating': rating,
        'form': form,
    }
    return render(request, 'ratings/movie.html', context)


def get_raters(request, rater_id):
    rater = get_object_or_404(Rater, pk=rater_id)
    ratings = rater.rating_set.all()
    context = {
        'rater': rater,
        'ratings': ratings,
        }
    return render(request, 'ratings/rater.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('ratings/')


def add_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            review = form.cleaned_data['review']
            rating_obj = Rating(rater=request.user.rater,
                                movie=movie,
                                rating=rating,
                                review=review)
            rating_obj.save()
            return HttpResponseRedirect('/ratings/movie/' + movie_id)
    else:
        form = RatingForm()

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'ratings/add_rating.html', context)


def user_redirect(request):
    url = '/ratings/rater/{}'.format(request.user.rater.id)
    return HttpResponseRedirect(url)


def delete(request, id):
    rating = get_object_or_404(Rating, id=id)
    if rating.rater.user != request.user:
        return HttpResponseRedirect('/ratings/')
    rating.delete()
    return HttpResponseRedirect('/ratings/')
