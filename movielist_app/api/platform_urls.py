from django.urls import path
from movielist_app.api.views import PlatformListView, PlatformDetailView

urlpatterns = [
    path('list/', PlatformListView.as_view(), name='getPlatformList'),
    path('<int:pk>', PlatformDetailView.as_view(),
         name='getPlatformDetail'),
]
