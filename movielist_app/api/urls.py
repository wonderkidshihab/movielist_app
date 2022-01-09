from django.urls import path
# from movielist_app.api.views import getMovieList, getMovie
from movielist_app.api.views import MovieListView, MovieDetailView

urlpatterns = [
    path('list/', MovieListView.as_view(), name='getMovieList'),
    path('<int:movie_id>', MovieDetailView.as_view(), name='getMovie'),
]
