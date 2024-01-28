from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Serieformulario(forms.Form):
    nombre = forms.CharField()
    año = forms.IntegerField()
    temporadas = forms.CharField()


class peliculaformulario(forms.Form):
    nombre = forms.CharField()
    año = forms.IntegerField()
    director = forms.CharField()
    genero = forms.CharField()
    duracion = forms.FloatField()

    
class musicaformulario(forms.Form):
    nombre = forms.CharField()
    año = forms.IntegerField()
    duracion = forms.FloatField()
    genero = forms.CharField()

class registrarusuario(UserCreationForm):
    username = forms.CharField(label="Ingresa tu nickname")
    email = forms.EmailField(label="Ingresa tu correo")
    password1 = forms.CharField(label="Ingresa tu contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma tu contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingresa tu nombre")
    last_name = forms.CharField(label="Ingresa tu apellido")
    class Meta:
            model = User
            fields = ["username","email","password1","password2","first_name","last_name"]    


class editarusuario(UserCreationForm):
    email = forms.EmailField(label="Ingresa tu correo")
    password1 = forms.CharField(label="Ingresa tu contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma tu contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingresa tu nombre")
    last_name = forms.CharField(label="Ingresa tu apellido")
    class Meta:
            model = User
            fields = ["email","password1","password2","first_name","last_name"]    


