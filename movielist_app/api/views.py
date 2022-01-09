from movielist_app import models
from movielist_app.api.serializers import ContentSerializer, PlatformSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ContentListView(APIView):
    def get(self, request):
        contents = models.Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializers = ContentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        else:
            return Response(serializers.errors, status=400)


class ContentDetailView(APIView):
    def get(self, request, content_id):
        try:
            Content = models.Content.objects.get(id=content_id)
        except Exception as e:
            return Response(status=404)
        serializer = ContentSerializer(Content)
        return Response(serializer.data, status=200)

    def put(self, request, Content_id):
        try:
            Content = models.Content.objects.get(id=Content_id)
        except Exception as e:
            return Response(status=404)
        serializer = ContentSerializer(Content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, content_id):
        try:
            Content = models.Content.objects.get(id=content_id)
        except Exception as e:
            return Response(status=404)
        Content.delete()
        return Response(status=204)


class PlatformListView(APIView):
    def get(self, request):
        platforms = models.Platform.objects.all()
        serializer = PlatformSerializer(platforms, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializers = PlatformSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        else:
            return Response(serializers.errors, status=400)


class PlatformDetailView(APIView):
    def get(self, request, platform_id):
        try:
            platform = models.Platform.objects.get(id=platform_id)
        except Exception as e:
            return Response(status=404)
        serializer = PlatformSerializer(platform)
        return Response(serializer.data, status=200)

    def put(self, request, platform_id):
        try:
            platform = models.Platform.objects.get(id=platform_id)
        except Exception as e:
            return Response(status=404)
        serializer = PlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, platform_id):
        try:
            platform = models.Platform.objects.get(id=platform_id)
        except Exception as e:
            return Response(status=404)
        platform.delete()
        return Response(status=204)
