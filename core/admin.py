from django.contrib import admin
from .models import Categoria,Especie, Articulo, mensaje
# Register your models here.

class modAdmin(admin.ModelAdmin):
      list_display= ['id','precio','nombreProducto','marca','especie','categoria']
      list_editable= ['precio','especie','categoria']
      list_filter= ['especie']

admin.site.register(Categoria)
admin.site.register(Especie)
admin.site.register(Articulo,modAdmin)
admin.site.register(mensaje)