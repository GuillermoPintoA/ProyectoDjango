
from django.urls import path,include
from .views import listar, contacto,modificar,listar_mensajes,detalle_articulo,lista_articulo,agregar, modificar, eliminar,test,productos,ArticuloViewSet,\
    registro

from rest_framework import routers
router=routers.DefaultRouter()
router.register('articulos',ArticuloViewSet)

urlpatterns =[

    #path('' , home, name="home"),   
    path('' , test, name="test"),
    path('productos' , productos, name="productos"),
    path('agregar' , agregar, name="agregar"),
    path('eliminar/<id>/' , eliminar, name="eliminar"),
    path('modificar/<id>/' , modificar, name="modificar"),
    path('listar' , listar, name="listar"),
    path('registro/', registro, name="registro"),
    path('mensajes' , contacto, name="contacto"),
    path('lista_articulo' , lista_articulo, name="lista_articulo"),
    path('detalle_articulo/<id>' , detalle_articulo, name="detalle_articulo"),
    path('listar_mensajes' , listar_mensajes, name="listar_mensajes"),
    path('api/',include(router.urls)),
]
