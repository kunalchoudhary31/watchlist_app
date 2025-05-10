# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.
 
# def movie_list(request):
#     movies = Movie.objects.all()
#     return JsonResponse(list(movies.values()), safe=False)

# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         "name": movie.name,
#         "description": movie.description,
#         "active": movie.active,
#     }
#     return JsonResponse(data=data, safe=False)
    