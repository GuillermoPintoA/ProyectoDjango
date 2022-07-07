
from django.urls import path
from .views import listar, contacto,listaArticulos,modificar,form_mod_articulo,agregar, form_articulo, modificar, eliminar,test,productos,\
    registro

urlpatterns =[

    #path('' , home, name="home"),   
    path('' , test, name="test"),
    path('productos' , productos, name="productos"),
    path('listaArticulos' , listaArticulos, name="listaArticulos"),
    path('form-Articulos' , form_articulo, name="form_articulo"),
    path('agregar' , agregar, name="agregar"),
    path('eliminar/<id>/' , eliminar, name="eliminar"),
    path('modificar/<id>/' , modificar, name="modificar"),
    path('listar' , listar, name="listar"),
    path('registro/', registro, name="registro"),
    path('mensajes' , contacto, name="contacto"),
]
