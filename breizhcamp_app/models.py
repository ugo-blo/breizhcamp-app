from django.db import models
from django.urls import reverse


# Create your models here
# There is a Release, Genre and Artist model


class Release(models.Model):
    """Model representing a release"""
    title = models.CharField(max_length=200, help_text="Enter a release title", verbose_name="Release title")
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField('Genre', help_text="Select a genre for this release")
    release_date = models.DateField(null=True, blank=True)
    song = models.ManyToManyField('Song', help_text="Select a song for this release")

    class Meta:
        ordering = ['release_date', 'title']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.title})'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Release."""
        return reverse('release-detail', args=[str(self.id)])


class Genre(models.Model):
    """Model representing a release genre"""
    name = models.CharField(max_length=200, help_text="Enter a release genre (e.g. IDM, Ambient, Techno, etc.)")

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Artist(models.Model):
    """Model representing an artist"""
    name = models.CharField(max_length=200, help_text="Enter an artist name", verbose_name="Artist name")

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Artist"""
        return reverse('artist-detail', args=[str(self.id)])


class Song(models.Model):
    title = models.CharField(max_length=200, help_text="Enter a song title", verbose_name="Song title")

    def __str__(self):
        """String for representing the Model object."""
        return self.title
