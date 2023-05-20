from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class session(models.Model):
    Name =(
        ('Latest Movies', "Latest Movies"),
        ("Web-series", "Web-series"),
    )
    name = models.CharField(choices=Name,max_length=100)

    def __str__(self):
        return self.name


class movie(models.Model):
    name = models.CharField(max_length=250)
    poster = models.ImageField(upload_to="movie/poster/image/")
    description = RichTextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    Releaseyear = models.IntegerField()
    Downloadlink = models.URLField()
    watchtralier = models.URLField()
    IMDB_rating = models.FloatField()
    current_season = models.CharField(max_length=250)
    detail = models.CharField(max_length=250)
    episode = models.CharField(max_length=250)
    session = models.ForeignKey(session,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class All_season(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    All_season = models.CharField(max_length=250)
    detail = models.CharField(max_length=250)
    episode = models.CharField(max_length=250)
    link = models.CharField(max_length=500)
    poster = models.CharField(max_length=250)



class media(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    photo = models.CharField(max_length=250)


class Genres(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    genre = (
        ('Action', "Action"),
        ("Thriller", "Thriller"),
        ("Horror", "Horror"),
        ("Drama", "Drama"),
        ("Romance", "Romance"),
        ("Sci-fi", "Sci-fi"),
        ("Crime film", "Crime film"),
        ("War", "War"),
        ("Westerns", "Westerns"),
        ("COMEDY", "COMEDY"),
        ("Sports", "Sports"),
        ("Adventure", "Adventure"),
        ("Documentary", "Documentary"),
        ("Romantic comedy", "Romantic comedy"),
        ("Fiction", "Fiction"),
        ("Mystery", "Mystery"),
        ("Epic", "Epic"),
        ("Dark comedy", "Dark comedy"),
        ("Experimental", "Experimental"),
        ("Animated film", "Animated film"),
        ("Sports", "Sports"),
        ("web-series", "web-series"),
        ("Biographical", "Biographical"),
        ("Disaster", "Disaster"),
        ("Coming-of-age story", "Coming-of-age story"),
        ("cartoon", "cartoon"),
        ("Anime", "Anime"),
        ("Road", "Road"),
        ("Spy", "Spy"),
        ("Silent", "Silent"),
        ("Propaganda", "Propaganda"),
        ("Dance film", "Dance film")

    )
    genres = models.CharField(choices=genre, max_length=100)
    color = models.CharField(max_length=100)





class keyword(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)

class downloadlink(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    link = models.URLField()
    title = models.CharField(max_length=250)
    size = models.CharField(max_length=250)

class subscribe(models.Model):
    email1 = models.EmailField()