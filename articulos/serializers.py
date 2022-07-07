from rest_framework import serializers
from core.models import Articulo

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articulo
        fields=['idArticulo','precio','nombreArticulo','especie','categoria']