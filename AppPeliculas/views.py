from django.shortcuts import render,redirect
from django.http import HttpResponse
from AppPeliculas.models import *
from AppPeliculas.forms import *
from django.shortcuts import get_object_or_404
import datetime as dt
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def agregar_serie (request):
   if request.method == "POST":
        serie_nueva = serie(nombre= request.POST["nombre"], año = request.POST["año"], temporadas=request.POST["temporada"])
        serie_nueva.save()
        return render(request,"nueva_serie.html")
   else:
       return render(request,"nueva_serie.html")

@login_required
def agregar_pelicula (request):
   if request.method == "POST":
        pelicula_nueva = pelicula(nombre= request.POST["nombre"], año = request.POST["año"], director=request.POST["director"],genero=request.POST["genero"],duracion=request.POST["duracion"])
        pelicula_nueva.save()
        return render(request,"nueva_pelicula.html")
   else:
       return render(request,"nueva_pelicula.html")

@login_required
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


def lista_serie (request):
    mis_series = serie.objects.all()
    info = {"series":mis_series}
    return render(request,"listado_serie.html",info)


def lista_musica (request):
    mis_canciones = musica.objects.all()
    info = {"canciones":mis_canciones}
    return render (request,"listado_musica.html",info)


def lista_pelicula (request):
    mis_peliculas = pelicula.objects.all()
    info = {"peliculas":mis_peliculas}  
    return render(request,"listado_pelicula.html",info)


def up_serie (request, serie_nombre):
    nuevo_formulario = None
    serie_up  = serie.objects.get(nombre=serie_nombre)
    print(serie_nombre)
    print(serie_up)
    if request.method == "POST":
        nuevo_formulario = Serieformulario(request.POST)
        print(Serieformulario(request.POST))
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data
            
            serie_up.nombre = info["nombre"]
            serie_up.año = info["año"]
            serie_up.temporadas = info["temporadas"]
            serie_up.save()
            
            return render(request, "inicio.html")
        else:
            nuevo_formulario = Serieformulario(initial={"nombre":serie_up.nombre})
    print("Valor de nuevo_formulario:", nuevo_formulario)
    return render(request,"up_serie.html", {"mi_formu":nuevo_formulario})

def up_serie1(request):
   if request.method == "POST":
        serie_up1 = serie(nombre= request.POST["nombre"])
        return redirect('up_serie', serie_nombre=serie_up1.nombre) 

   else:
      return render(request,"up_serie1.html") 


def up_pelicula1 (request):
   if request.method == "POST":
        pelicula_up1 = pelicula(nombre= request.POST["nombre"])
        return redirect('up_pelicula', pelicula_nombre=pelicula_up1.nombre)
   else:
       return render(request,"up_pelicula1.html")  
   
def up_musica1 (request):
   if request.method == "POST":
        musica_up1 = musica(nombre= request.POST["nombre"])
        return redirect('up_musica', musica_nombre=musica_up1.nombre)
        
   else:
       return render(request,"up_musica1.html")  
   
def del_serie(request):
   if request.method == "POST":
        serie_up1 = serie(nombre= request.POST["nombre"])
        serie_up1.delete()
        return render(request,"del_serie.html")
   else:
      return render(request,"del_serie.html")

def del_pelicula (request):
   if request.method == "POST":
        pelicula_up1 = pelicula(nombre= request.POST["nombre"])
        pelicula_up1.delete()
        return render(request,"del_pelicula.html")
   else:
      return render(request,"del_pelicula.html") 
   
def del_musica (request):
   if request.method == "POST":
        musica_up1 = musica(nombre= request.POST["nombre"])
        musica_up1.delete()
        return render(request,"del_musica.html")
   else:
      return render(request,"del_musica.html")



def up_pelicula (request, pelicula_nombre):
    nuevo_formulario = None
    pelicula_up  = pelicula.objects.get(nombre=pelicula_nombre)
    print(pelicula_nombre)
    print(pelicula_up)
    if request.method == "POST":
        nuevo_formulario = peliculaformulario(request.POST)
        print(peliculaformulario(request.POST))
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data
            
            pelicula_up.nombre = info["nombre"]
            pelicula_up.año = info["año"]
            pelicula_up.director = info["director"]
            pelicula_up.genero = info["genero"]
            pelicula_up.duracion = info["duracion"]
            pelicula_up.save()
            return render(request, "inicio.html")
        else:
            nuevo_formulario = peliculaformulario()
    print("Valor de nuevo_formulario:", nuevo_formulario)
    return render(request,"up_pelicula.html", {"mi_formu":nuevo_formulario})




def up_musica (request, musica_nombre):
    nuevo_formulario = None
    musica_up  = musica.objects.get(nombre=musica_nombre)
    print(musica_nombre)
    print(musica_up)
    if request.method == "POST":
        nuevo_formulario = musicaformulario(request.POST)
        print(musicaformulario(request.POST))
        if nuevo_formulario.is_valid():
            info = nuevo_formulario.cleaned_data
            
            musica_up.nombre = info["nombre"]
            musica_up.año = info["año"]
            musica_up.duracion = info["duracion"]
            musica_up.genero = info["genero"]
            musica_up.save()
            
            return render(request, "inicio.html")
        else:
            nuevo_formulario = musicaformulario()
    print("Valor de nuevo_formulario:", nuevo_formulario)
    return render(request,"up_musica.html", {"mi_formu":nuevo_formulario})

def registrar(request):

    if request.method == 'POST':
        formulario = registrarusuario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = info["username"]
            formulario.save()
            return render(request,"inicio.html", {"mensaje1":f"{usuario}"})
    else:
        formulario = registrarusuario()

    return render(request, "registro/registrar.html", {"formu":formulario})

def editar_perfil(request):
    user_actual = request.user
    if request.method == 'POST':
        formulario = editarusuario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            user_actual.first_name = info["first_name"]
            user_actual.last_name = info["last_name"]
            user_actual.email = info["email"]
            user_actual.set_password(info["password1"])
            user_actual.save()
            return render(request,"inicio.html", {"mensaje1":f"{user_actual}"})
    else:
        formulario = editarusuario(initial={"first_name":user_actual.first_name,
                                               "last_name":user_actual.last_name,
                                               "email":user_actual.email})

    return render(request, "registro/actualizar.html", {"formu":formulario})




def login_user(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():  # Si pasó la validación de Django

            info = formulario.cleaned_data
            usuario = info["username"]
            contraseña = info["password"]


            user = authenticate(username= usuario, password=contraseña)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje1":f"{usuario}"})
        else:
            return render(request, "inicio.html", {"mensaje2":"Tus Datos son incorrectos"})

    else:
        formulario = AuthenticationForm()
    return render(request, "registro/inicio_sesion.html", {"formu":formulario})
       


def inicio(request):
    hora1 = dt.datetime.now()
    hora = {'hora': hora1}
    return render(request, "inicio.html", hora)


def about_me(request):
    hora1 = dt.datetime.now()
    hora = {'hora': hora1}
    return render(request, "about.html", hora)

def profile(request):
    user_actual = request.user
    nick = user_actual.username
    nombre = user_actual.first_name
    apellido = user_actual.last_name
    email = user_actual.email
    print(nombre)
    hora1 = dt.datetime.now()
    hora = {'hora': hora1}
    return render(request, "me.html", {'hora': hora, 'nombre': nombre, 'nick': nick, 'apellido': apellido, 'email': email})