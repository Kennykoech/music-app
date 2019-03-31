
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    song_logo = models.FileField(max_length=100)
    song_title = models.CharField(max_length=100)
    song = models.FileField()

    def get_absolute_url(self):
        return reverse('ngoma:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.artist + ' _ ' + self.genre +  ' _ ' +  self.song_logo + ' _ ' + self.song_title + ' _ ' + str(self.song.song) 

    



