from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Articulo,mensaje
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArticulosForm(ModelForm):
    class Meta:
        model=Articulo
        fields=['id','precio','nombreProducto','marca','especie','categoria','imagen']

class mensajeForm(ModelForm):
    class Meta:
        model=mensaje
        fields=['nombre','apellido','correo','tipo_consulta','motivo','mensaje','avisos']

class productoform(forms.ModelForm):
    class meta:
        model=Articulo
        fields=['__all__']

class CustomUserCreationForm(UserCreationForm):
       

    class Meta:
        model=User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]