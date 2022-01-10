from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', include('movielist_app.api.urls')),
    path('platform/', include('movielist_app.api.platform_urls')),
    path('review/', include('movielist_app.api.review_urls')),
]
