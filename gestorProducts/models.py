from django.db import models
from gestorUser.models import Usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ##  vinculado con categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ##  vinculado con usuario
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
 