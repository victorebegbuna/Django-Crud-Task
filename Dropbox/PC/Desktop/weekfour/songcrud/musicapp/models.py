from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length=40)
    date_released = models.IntegerField()
    likes = models.CharField(max_length=40)
    artiste_id = models.IntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.CharField
    song_id = models.IntegerField
    