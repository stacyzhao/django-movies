from django.conf.urls import url
from . import views

app_name = 'ratings'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^top_movies/$', views.top_movies, name='top_movies'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.get_movies, name='movie_detail'),
    url(r'^rater/(?P<rater_id>[0-9]+)/$', views.get_raters, name='rater_detail'),
    url(r'^add_rating/(?P<movie_id>[0-9]+)/$', views.add_rating, name='add_rating'),
    url(r'^user_redirect/', views.user_redirect, name='user_redirect'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^(?P<id>[0-9]+)/delete', views.delete, name='delete'),
]
