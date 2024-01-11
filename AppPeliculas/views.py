from django.shortcuts import render
from django.http import HttpResponse
from AppPeliculas.models import *

import datetime as dt
# Create your views here.

def agregar_serie (request):
   if request.method == "POST":
        serie_nueva = serie(nombre= request.POST["nombre"], año = request.POST["año"], temporadas=request.POST["temporada"])
        serie_nueva.save()
        return render(request,"nueva_serie.html")
   else:
       return render(request,"nueva_serie.html")

def agregar_pelicula (request):
   if request.method == "POST":
        pelicula_nueva = pelicula(nombre= request.POST["nombre"], año = request.POST["año"], director=request.POST["director"],genero=request.POST["genero"],duracion=request.POST["duracion"])
        pelicula_nueva.save()
        return render(request,"nueva_pelicula.html")
   else:
       return render(request,"nueva_pelicula.html")

def agregar_musica (request):
   if request.method == "POST":
        musica_nueva = musica(nombre= request.POST["nombre"], año = request.POST["año"], duracion=request.POST["duracion"], genero=request.POST["genero"])
        musica_nueva.save()
        return render(request,"nueva_cancion.html")
   else:
       return render(request,"nueva_cancion.html")


def revisar_serie (request):

       return render(request,"revisar_serie.html")

def resultado_serie (request):
    if request.method=="GET":
        año = request.GET["año"]
        resultados_serie = serie.objects.filter(año__icontains=año)
        return render (request,"resultado_serie.html",{"series":resultados_serie} )


def revisar_pelicula (request):

       return render(request,"revisar_pelicula.html")

def resultado_pelicula (request):
    if request.method=="GET":
        año = request.GET["año"]
        resultados_pelicula = pelicula.objects.filter(año__icontains=año)
        return render (request,"resultado_pelicula.html",{"pelicula":resultados_pelicula} )
def revisar_musica (request):

       return render(request,"revisar_musica.html")

def resultado_musica (request):
    if request.method=="GET":
        año = request.GET["año"]
        resultados_musica = musica.objects.filter(año__icontains=año)
        return render (request,"resultado_musica.html",{"musica":resultados_musica} )




def ver_pelicula (request):
    mis_peliculas = pelicula.objects.all() #obtener todos los datos de la tabla
    #info = {"serie":mis_peliculas}
    hora1 = dt.datetime.now()
    return render(request, "peliculas.html", {'hora': hora1 , 'serie':mis_peliculas})

def ver_serie (request):
    mis_series = serie.objects.all() #obtener todos los datos de la tabla
    #info = {"serie":mis_series}
    hora1 = dt.datetime.now()
    return render(request, "series.html", {'hora': hora1 , 'serie':mis_series})

def escuchar_musica (request):
    mis_canciones = musica.objects.all() #obtener todos los datos de la tabla
    #info = {"serie":mis_canciones}
    hora1 = dt.datetime.now()
    return render(request, "musica.html", {'hora': hora1 , 'serie':mis_canciones})

def inicio(request):
    hora1 = dt.datetime.now()
    hora = {'hora': hora1}
    return render(request, "inicio.html", hora)

