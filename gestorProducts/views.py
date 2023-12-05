from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Producto, Categoria
from gestorUser.decorators import admin_required
from gestorUser.models import Usuario
from django.http import HttpResponseForbidden

@login_required
@admin_required
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestorProducts/listar_categorias.html', {'categorias': categorias})

@login_required
@admin_required
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        Categoria.objects.create(nombre=nombre)
        return redirect('listar_categorias')
    return render(request, 'gestorProducts/crear_categoria.html')

@login_required
@admin_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.save()
        return redirect('listar_categorias')
    return render(request, 'gestorProducts/editar_categoria.html', {'categoria': categoria})

@login_required
@admin_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    categoria.delete()
    return redirect('listar_categorias')



@login_required

def listar_productos(request):
    if request.user.is_superuser:  # Verificar si es admin
        productos = Producto.objects.all()
        return render(request, 'gestorProducts/listar_productos.html', {'productos': productos})
    else:
        productos = Producto.objects.filter(creador=request.user.usuario)
        return render(request, 'gestorProducts/listar_productos_user.html', {'productos': productos})
    




@login_required
def crear_producto(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        categoria_id = request.POST['categoria']
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        Producto.objects.create(nombre=nombre, descripcion=descripcion, categoria=categoria, creador=request.user.usuario)
        return redirect('listar_productos')
    return render(request, 'gestorProducts/crear_producto.html', {'categorias': categorias})

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.categoria_id = request.POST['categoria']
        producto.save()
        return redirect('listar_productos')
    return render(request, 'gestorProducts/editar_producto.html', {'producto': producto, 'categorias': categorias})

@login_required
@admin_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.delete()
    return redirect('listar_productos')




