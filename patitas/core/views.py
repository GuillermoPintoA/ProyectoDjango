from cmd import IDENTCHARS
from distutils import core
from django.forms import PasswordInput
from django.http import Http404
from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator

from core.forms import ArticulosForm
from .models import Articulo,mensaje
from .forms import CustomUserCreationForm, mensajeForm
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required

from rest_framework import viewsets
from .serializers import ArticuloSerializer

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

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

def listar_mensajes(request):

    return render(request,'core/listar_mensajes.html')  

def test(request):

    return render(request,'core/test.html')   

def productos(request):
    articulos=Articulo.objects.all()
    contexto={
        'articulos':articulos
    }
    return render(request,'core/productos.html',contexto)  

@permission_required('core.view_articulo')
def listar(request):
    articulos=Articulo.objects.all()

    contexto={
        'articulos':articulos,

    }
    return render(request,'core/Funciones/listar.html',contexto)  


def listar_mensajes(request):
    mensajes=mensaje.objects.all()


    contexto={
        'mensajes':mensajes,

    }
    return render(request,'core/listar_mensajes.html',contexto)  


@permission_required('core.add_articulo')
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

@permission_required('core.change_articulo')
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

@permission_required('core.delete_articulo')
def eliminar(request,id):
    articulo=Articulo.objects.get(id=id)
    articulo.delete()
    messages.success(request, "Eliminado Correctamente")

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

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_articulo(request):
    if request.method=='GET':
        articulo=Articulo.objects.all()
        serializer=ArticuloSerializer(articulo, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ArticuloSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def detalle_articulo(request,id):
    #valido que la patente exista
    try:
        articulo=Articulo.objects.get(id=id)
    except ArticuloSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #verificar el método invocado
    if request.method=='GET': #devolver info de UN vehiculo por su patente
        serializer=ArticuloSerializer(articulo)
        return Response(serializer.data)
    elif request.method=='PUT':#actualizar UN vehiculo por su patente
        data=JSONParser().parse(request)
        serializer=ArticuloSerializer(articulo,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':#Eliminar UN vehiculo por su patente
        Articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

