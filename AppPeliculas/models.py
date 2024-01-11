from django.db import models

# Create your models here.
#un modelo es una clase en el archivo models
class pelicula(models.Model):
    
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    director = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    duracion = models.FloatField()

class serie(models.Model):
    
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    temporadas = models.CharField(max_length=40)
    
class musica(models.Model):
    
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    duracion = models.FloatField()
    genero = models.CharField(max_length=40)