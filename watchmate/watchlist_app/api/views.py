from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class MovieList(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serilalizer = MovieSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_201_CREATED)
class MovieDetail(APIView):

    def get(self,request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)