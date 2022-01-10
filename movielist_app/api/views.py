from movielist_app import models
from movielist_app.api.serializers import ContentSerializer, PlatformSerializer, ReviewSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError


class ContentListView(generics.ListAPIView):
    queryset = models.Content.objects.all()
    serializer_class = ContentSerializer


class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Content.objects.all()
    serializer_class = ContentSerializer


class PlatformListView(generics.ListAPIView):
    queryset = models.Platform.objects.all()
    serializer_class = PlatformSerializer


class PlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Platform.objects.all()
    serializer_class = PlatformSerializer


class ReviewListView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return models.Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        reviewer = self.request.user
        content = models.Content.objects.get(pk=pk)
        review_queryset = models.Review.objects.filter(
            content=content, reviewer=reviewer)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this content")
        else:
            serializer.save(content=content, reviewer=reviewer)


class ReviewListForContentView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return models.Review.objects.filter(content=self.kwargs['pk'])
