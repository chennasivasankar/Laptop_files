from django.db import models
from imdb.utils import *
from datetime import datetime

class Director(models.Model):
    name=models.CharField(max_length=100,unique=True)
    gender_choices=(
        ("male","Male"),
        ("female","Female")
    )
    gender=models.CharField(max_length=10,choices=gender_choices)
    no_of_facebook_likes=models.CharField(max_length=10)

class Actor(models.Model):
    actor_id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    gender_choices=(
        ('male','Male'),
        ('female','Female')
    )
    gender=models.CharField(max_length=20,choices=gender_choices)
    fb_likes=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    

class Movie(models.Model):
    import random
    name=models.CharField(max_length=100)
    movie_id=models.CharField(max_length=100,primary_key=True)
    actors=models.ManyToManyField(Actor,
                    through='Cast',
                    through_fields=('movie','actor'),
                    )
    box_office_collection_in_crores=models.FloatField()
    director=models.ForeignKey(
                Director,
                on_delete=models.CASCADE
                ) 
    rating=models.FloatField()
    release_date=models.DateField()
    genre=models.CharField(max_length=20)
    movie_story_line=models.TextField()
    movie_image_url=models.URLField(max_length=200)

class Cast(models.Model):
    import random
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_debut_movie=models.BooleanField(default=False)
    role=models.CharField(max_length=20)
    remuneration=models.IntegerField()


