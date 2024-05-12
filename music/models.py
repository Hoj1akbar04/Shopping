
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class Album(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.URLField(null=True)
    watching = models.PositiveBigIntegerField(default=0)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class Song(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.URLField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    listened = models.PositiveBigIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]
