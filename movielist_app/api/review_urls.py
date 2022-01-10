from django.urls import path
from movielist_app.api.views import ReviewListView, ReviewDetailsView

urlpatterns = [
    path('list/', ReviewListView.as_view(), name='getReviewformList'),
    path('<int:pk>', ReviewDetailsView.as_view(), name='getReviewformDetail')
]
