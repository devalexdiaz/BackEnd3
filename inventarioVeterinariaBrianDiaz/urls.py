"""
URL configuration for djangoLogin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new

from gestorUser.views import *
from gestorProducts.views import *

### Me gusta trabajar con todas las url en este archivo ya que es mas rapido de encontrar un url, en caso de usar mas de uno suelo ocupar include

""" Prueba para template  """
#TemplateView.as_view(template_name="home.html")

urlpatterns = [
    ## Url de admin panel de django
    path('admin/', admin.site.urls),
    

    ## Urls de web sin login
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('servicios/', servicios, name="servicios"),


    ## Urls de cuentas
    path('cuentas/', include("django.contrib.auth.urls")),
    path("dashboard/", personasIndex , name="dashboard"),
    path("signUp/", signUp , name="signUp"),     
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),


    ## Urls de categorias 
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/crear/', crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:categoria_id>/', editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:categoria_id>/', eliminar_categoria, name='eliminar_categoria'),
    
    ## Urls de productos
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    
    
    ## Url para gestionar mi perfil de usuario
    path('editar-usuario/', editar_usuario, name='editar_usuario'),
    path('ver-perfil/', ver_perfil, name='ver_perfil'),
    
    
]
