from django.urls import path
# from movielist_app.api.views import getMovieList, getMovie
from movielist_app.api.views import ContentListView, ContentDetailView

urlpatterns = [
    path('list/', ContentListView.as_view(), name='getMovieList'),
    path('<int:content_id>', ContentDetailView.as_view(), name='getMovie'),
]
