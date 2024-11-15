from django.db import models
#movie data should contain the following movie name, Duration, Genre, Director, Lead actor, Language
# Create your models here.

class Movies(models.Model):
    V_movie_name = models.CharField(max_length=100,default="No name")
    V_duration = models.CharField(max_length=50)
    V_genre = models.CharField(max_length=50)
    V_director = models.CharField(max_length=60)
    V_lead_actor = models.CharField(max_length=100)
    V_language = models.CharField(max_length=100)

class Movie_T(models.Model):
    V_Movie_Name = models.CharField(max_length=100,default="No name")
    V_trailer = models.FileField(upload_to='uploads/', blank=True, null=True)  
    V_launch_date = models.DateField()  

    def __str__(self):
        return self.V_Movie_Name