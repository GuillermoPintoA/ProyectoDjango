from distutils.command.upload import upload
from django.db import models

# Create your models here.

#modelo para categoria
class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria=models.CharField(max_length=30, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria
#modelo para especie
class Especie(models.Model):
    idEspecie=models.IntegerField(primary_key=True, verbose_name='Id de la especie')
    nombreEspecie=models.CharField(max_length=30, verbose_name='Nombre de la especie')

    def __str__(self):
        return self.nombreEspecie

#modelo para articulos
class Articulo(models.Model):
    id=models.CharField(max_length=50, primary_key=True, verbose_name='numero de producto')
    precio=models.IntegerField(max_length=50, verbose_name="Precio ")
    nombreProducto=models.CharField(max_length=30, verbose_name='Nombre')
    especie= models.ForeignKey(Especie,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreProducto=models.CharField(max_length=30, verbose_name='Nombre')
    marca=models.CharField(max_length=30, verbose_name='marca')
    imagen=models.ImageField(upload_to="productos",null=True)


    def __str__(self):
        return self.id 
opciones_consultas=[
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"],
    [4,"Solicitud"]
]

#modelo para contactos
class mensaje(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consultas)
    motivo=models.CharField(max_length=50)
    mensaje=models.TextField()
    avisos=models.BooleanField()

    def __str__(self):
        return self.nombre 

