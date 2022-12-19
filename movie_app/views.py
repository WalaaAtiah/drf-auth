from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .serializers  import MovieSerializer
from .models import Movie
from .permissions import IsOwnerOrReadOnly


class MovieListView(ListCreateAPIView):
   queryset=Movie.objects.all()
   serializer_class=MovieSerializer


class MovieDetailView(RetrieveUpdateDestroyAPIView):
   queryset=Movie.objects.all()
   serializer_class= MovieSerializer
   permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]