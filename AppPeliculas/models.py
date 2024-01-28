from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#un modelo es una clase en el archivo models
class pelicula(models.Model):
    def __str__(self):
        return f"{self.nombre} --- {self.año}"
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    director = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    duracion = models.FloatField()

class serie(models.Model):
    def __str__(self):
        return f"{self.nombre} --- {self.año}"
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    temporadas = models.CharField(max_length=40)
    
class musica(models.Model):
    def __str__(self):
        return f"{self.nombre} --- {self.año}"
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    duracion = models.FloatField()
    genero = models.CharField(max_length=40)

class Avatars(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True,blank=True)


