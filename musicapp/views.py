#from django.shortcuts import render
from django.http import HttpResponse

#from rest_framework import viewsets
from rest_framework import generics

from .models import Song
from .models import Artiste
from .serializers import SongSerializer, ArtisteSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer



# Create your views here.
def index(request):
    return HttpResponse("Welcome to Musicapp")

