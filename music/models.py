from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    pic = models.URLField(max_length=500, verify_exists=True, \
            null=True, blank=True)

    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist, null=True, blank=True)
    url = models.URLField(max_length=500, verify_exists=True, \
            null=True, blank=True)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)
    release_date = models.DateField(null=True, blank=True)
    album_artist = models.ManyToManyField(Artist, null=True, blank=True)
    album_art = models.URLField(max_length=500, verify_exists=True, \
            null=True, blank=True)

    def __unicode__(self):
        return self.name 

