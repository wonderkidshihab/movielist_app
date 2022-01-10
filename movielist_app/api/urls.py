from django.urls import path
# from movielist_app.api.views import getMovieList, getMovie
from movielist_app.api.views import ContentListView, ContentDetailView, ReviewCreateView, ReviewListForContentView

urlpatterns = [
    path('list/', ContentListView.as_view(), name='getMovieList'),
    path('<int:pk>', ContentDetailView.as_view(), name='getMovie'),
    path('<int:pk>/review-create', ReviewCreateView.as_view(), name='createReview'),
    path('<int:pk>/reviews', ReviewListForContentView.as_view(), name='listofreviews'),
]
