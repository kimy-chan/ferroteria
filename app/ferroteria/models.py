
from django.db import models

# Create your models here.


class herramienta(models.Model):
    id = models.BigAutoField(primary_key=True )
    nombre = models.CharField(max_length=100, verbose_name='Nombre' )
    color = models.CharField(max_length=100, verbose_name='Color' )
    marca=models.CharField(max_length=100,verbose_name='Marca')
    precio = models.IntegerField(verbose_name='Precio')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen')
    cantidad =models.IntegerField(verbose_name='cantida')
    
    def __str__(self) -> str:
        return self.nombre

class Pinturas(models.Model):
    id = models.BigAutoField(primary_key=True )
    color = models.CharField(max_length=100, verbose_name='Color')
    marca=models.CharField(max_length=100, verbose_name='Marca')
    precio = models.IntegerField(verbose_name='Precio')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen')
    cantidad =models.IntegerField(verbose_name='Cantidad')
    def __str__(self) -> str:
        return self.color
   




