from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

""" El formulario de django trae por defecto los siguientes campos:
nombre de usuario Nombre Apellido Email Contraseña """
# Create your models here.

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=500, blank=True)
    sitioWeb = models.URLField(blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.username
    
@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)
        
@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, **kwargs):
    instance.usuario.save()