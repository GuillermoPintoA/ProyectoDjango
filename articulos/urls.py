from django.urls import path
from articulos.views import lista_articulos,detalle_articulo

urlpatterns=[
    path('lista_articulos',lista_articulos,name='lista_articulos'),
    path('detalle_articulo/<id>',detalle_articulo, name='detalle_articulo'),
]