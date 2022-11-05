from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, null=True, on_delete=models.CASCADE)
    date_released = models.DateField(default=datetime.today)
    likes = models.CharField(max_length=400)
    title = models.CharField(max_length = 400)
    
    def __str__(self):
        return self.title

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, null=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.content
    