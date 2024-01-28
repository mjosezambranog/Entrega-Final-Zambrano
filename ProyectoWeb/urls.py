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
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("series/", ver_serie, name="Series"),
    path("peliculas/", ver_pelicula, name="Peliculas"),
    path("musica/", escuchar_musica, name="Musica"),
    path("", inicio, name="Inicio"),
    path("login/", login_user, name="login_user" ),
    path("signup/", registrar, name="registrar" ),
    path("about/", about_me, name="about" ),
    path("profile/", profile, name="profile" ),
    path("logout/", LogoutView.as_view(template_name="registro/cerrar_sesion.html"), name= "logout"),
    path("Update_profile/", editar_perfil, name="actualizar" ),
    
    #CRUD
    #C: Crear 
    path("crearserie/", agregar_serie, name="nueva_serie" ),
    path("crearpelicula/", agregar_pelicula, name="nueva_pelicula" ),
    path("crearmusica/", agregar_musica, name="nueva_musica" ),
    #R: Read
    path("revisarserie/", revisar_serie, name="revisar_serie" ),
    path("revisarpelicula/", revisar_pelicula, name="revisar_pelicula" ),
    path("revisarmusica/", revisar_musica, name="revisar_musica" ),
    path("resultadoserie/", resultado_serie, name="resultado_serie" ),
    path("resultadopelicula/", resultado_pelicula, name="resultado_pelicula" ),
    path("resultadomusica/", resultado_musica, name="resultado_musica" ),

    path("listaserie/", lista_serie, name="lista_serie" ),
    path("listapelicula/", lista_pelicula, name="lista_pelicula" ),
    path("listamusica/", lista_musica, name="lista_musica" ),
    #U: Update
    path("upserie/", up_serie1, name="up_serie1" ),
    path("uppelicula/", up_pelicula1, name="up_pelicula1" ),
    path("upmusica/", up_musica1, name="up_musica1" ),
    path("upserie/<serie_nombre>/", up_serie, name="up_serie" ),
    path("uppelicula/<pelicula_nombre>/", up_pelicula, name="up_pelicula" ),
    path("upmusica/<musica_nombre>/", up_musica, name="up_musica" ),
    #D: Delete
    path("delserie/", del_serie, name="del_serie" ),
    path("delpelicula/", del_pelicula, name="del_pelicula" ),
    path("delmusica/", del_musica, name="del_musica" ),




    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)