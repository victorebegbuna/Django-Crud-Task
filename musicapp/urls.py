from django.urls import path

#from songcrud.musicapp.models import Artiste

#from songcrud.musicapp.models import Artiste
from .import views
from rest_framework.routers import DefaultRouter
from musicapp.views import ArtisteViewSet
from musicapp.views import SongViewSet

router = DefaultRouter()
router.register(r'Artiste', ArtisteViewSet, basename='Artiste')
router = DefaultRouter()
router.register(r'Song', SongViewSet, basename='Song')



#urlpatterns = [
    #path("", views.index, name="index")
#]


urlpatterns = [
    path("api-auth", views.index, name="index")
] + router.urls

#127.0.0.1:8000/Artiste
