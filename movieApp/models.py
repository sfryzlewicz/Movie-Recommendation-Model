from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    #email = models.EmailField(unique=True)
    #date_of_birth = models.DateField(null=True, blank=True)
    #profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # Add other fields as needed
    pass

class Movie(models.Model):
    movieId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    #year = models.IntegerField(null=True, blank=True)

class Genres(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name