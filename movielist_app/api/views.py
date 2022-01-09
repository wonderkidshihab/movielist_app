from movielist_app import models
from movielist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView


class MovieListView(APIView):
    def get(self, request):
        movies = models.Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializers = MovieSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        else:
            return Response(serializers.errors, status=400)


class MovieDetailView(APIView):
    def get(self, request, movie_id):
        try:
            movie = models.Movie.objects.get(id=movie_id)
        except Exception as e:
            return Response(status=404)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=200)

    def put(self, request, movie_id):
        try:
            movie = models.Movie.objects.get(id=movie_id)
        except Exception as e:
            return Response(status=404)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, movie_id):
        try:
            movie = models.Movie.objects.get(id=movie_id)
        except Exception as e:
            return Response(status=404)
        movie.delete()
        return Response(status=204)


# @api_view(['GET', 'POST'])
# def getMovieList(request):
#     if request.method == 'GET':
#         movies = models.Movie.objects.all()
#         serializers = MovieSerializer(movies, many=True)
#         return Response(serializers.data)
#     elif request.method == 'POST':
#         serializers = MovieSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def getMovie(request, movie_id):
#     movie = models.Movie.objects.get(id=movie_id)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializers = MovieSerializer(movie, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response({'deleted': True})
