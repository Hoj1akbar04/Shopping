
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.URLField(null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.URLField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


