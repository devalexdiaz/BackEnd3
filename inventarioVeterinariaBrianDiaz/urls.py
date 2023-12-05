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

from gestorProducts.views import listar_categorias, crear_categoria, editar_categoria, eliminar_categoria, \
    listar_productos, crear_producto, editar_producto, eliminar_producto


""" Prueba para template  """
#TemplateView.as_view(template_name="home.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    
    path('cuentas/', include("django.contrib.auth.urls")),
    path("dashboard/", personasIndex , name="dashboard"),
    path("signUp/", signUp , name="signUp"),     
    
    path('about/', about, name="about"),
    path('servicios/', servicios, name="servicios"),

    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/crear/', crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:categoria_id>/', editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:categoria_id>/', eliminar_categoria, name='eliminar_categoria'),
    
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
]
