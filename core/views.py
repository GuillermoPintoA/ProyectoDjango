from cmd import IDENTCHARS
from distutils import core
from django.forms import PasswordInput
from django.shortcuts import render, redirect,get_object_or_404

from core.forms import ArticulosForm,productoform
from .models import Articulo
from .forms import CustomUserCreationForm, mensajeForm
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required

@login_required
def contacto(request):
    contexto={
        'form':mensajeForm
    }
    if request.method=='POST':
        formulario= mensajeForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha enviado el mensaje")
            contexto["mensajes"]="mensaje enviado"
    else:
        contexto['form']
    return render(request,'core/mensajes.html',contexto) 

def test(request):

    return render(request,'core/test.html')   

def productos(request):
    articulos=Articulo.objects.all()
    contexto={
        'articulos':articulos
    }
    return render(request,'core/productos.html',contexto)  

@permission_required('app.view_producto')
def listar(request):
    articulos=Articulo.objects.all()
    contexto={
        'articulos':articulos
    }
    return render(request,'core/Funciones/listar.html',contexto)  

def listaArticulos(request):
    articulos=Articulo.objects.all()
    contexto={
        'articulos':articulos
    }
    return render(request, 'core/productos.html', contexto)

@permission_required('app.add_producto')
def agregar(request):
    contexto={
        'form':ArticulosForm
    }
    if request.method=='POST':
        formulario=ArticulosForm(data=request.POST,files=request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Agregado Correctamente")
            contexto['mensajes']="Guardado con Exito"
    return render(request,'core/Funciones/agregar.html',contexto)

@permission_required('app.change_producto')
def modificar(request,id):
    articulo=Articulo.objects.get(id=id) 
    contexto={
        'form':ArticulosForm(instance=articulo)
    }
    if request.method=='POST':
        formulario=ArticulosForm(data=request.POST, instance=articulo)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            contexto['mensajes']="Modificado Correctamente"

    return render(request, 'core/Funciones/modificar.html',contexto)

@permission_required('app.delete_producto')
def eliminar(request,id):
    articulo=Articulo.objects.get(id=id)
    articulo.delete()
    messages.success(request, "Eliminado Correctamente")

    return redirect(to='productos')

def form_articulo(request):
    contexto={
        'form':ArticulosForm()
    }
    if request.method=='POST':
        formulario=ArticulosForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje']="Guardado con Exito"
            
    return render(request, 'core/form_articulo.html', contexto)

def form_mod_articulo(request,id):
    articulo=Articulo.objects.get(id=id) 
    contexto={
        'form':ArticulosForm(instance=articulo)
    }
    if request.method=='POST':
        formulario=ArticulosForm(data=request.POST, instance=articulo)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje']="Modificado Correctamente"

    return render(request, 'core/form_mod_articulo.html', contexto)

def form_del_articulo(request,id):
    articulo=Articulo.objects.get(idArticulo=id)
    articulo.delete()

    return redirect(to='productos')

def registro(request):
    data ={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente ")
            return redirect(to="test")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

