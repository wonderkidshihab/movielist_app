from django.urls import path
from movielist_app.api.views import PlatformListView, PlatformDetailView

urlpatterns = [
    path('list/', PlatformListView.as_view(), name='getPlatformList'),
    path('<int:platform_id>', PlatformDetailView.as_view(),
         name='getPlatformDetail'),
]
