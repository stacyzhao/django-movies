from django.conf.urls import url, patterns

from . import views

app_name = 'ratings'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^movie/$', views.get_movies, name='movie'),
    # url(r'^rating/$', views.get_ratings, name='rating'),
    # url(r'^rater/$', views.get_raters, name='rater'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.get_movies, name='movie_detail'),
    url(r'^rater/(?P<rater_id>[0-9]+)/$', views.get_raters, name='rater_detail'),
    # patterns('', (url(r'^$', ratings.views.movie, name='movie')))
    ]
