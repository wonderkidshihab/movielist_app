# from django.shortcuts import render
# from movielist_app.models import Movie
# from django.http import JsonResponse
# # Create your views here.


# def getMovieList(request):
#     movie = Movie.objects.all()
#     return JsonResponse(list(movie.values()), safe=False)


# def getMovie(request, pk):
#     movie = Movie.objects.get(id=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active,
#     }
#     return JsonResponse(data, safe=False)
