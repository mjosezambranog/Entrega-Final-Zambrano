"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppPeliculas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("series/", ver_serie, name="Series"),
    path("peliculas/", ver_pelicula, name="Peliculas"),
    path("musica/", escuchar_musica, name="Musica"),
    path("", inicio, name="Inicio"),

    path("crearserie/", agregar_serie, name="nueva_serie" ),
    path("crearpelicula/", agregar_pelicula, name="nueva_pelicula" ),
    path("crearmusica/", agregar_musica, name="nueva_musica" ),
    path("revisarserie/", revisar_serie, name="revisar_serie" ),
    path("revisarpelicula/", revisar_pelicula, name="revisar_pelicula" ),
    path("revisarmusica/", revisar_musica, name="revisar_musica" ),
    path("resultadoserie/", resultado_serie, name="resultado_serie" ),
    path("resultadopelicula/", resultado_pelicula, name="resultado_pelicula" ),
    path("resultadomusica/", resultado_musica, name="resultado_musica" )
    ]
