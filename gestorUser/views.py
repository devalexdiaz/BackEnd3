from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
from .models import Usuario
from .forms import SignUpForm
from .decorators import admin_required
from .forms import UsuarioForm
from .forms import UsuarioForm, ExtendedUsuarioForm


@login_required
def personasIndex(request):


    if request.user.is_superuser:
        return render(request, 'gestorUser/dashboardAdmin.html')
    if request.user.is_staff:
        return render(request, 'gestorUser/dashboardStaff.html')
    else:
        return render(request, 'gestorUser/dashboardUser.html')
    
    
       


def signUp(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Obtener el valor del checkbox
            is_admin = form.cleaned_data['is_admin']
            # Crear usuario y asignar valor a is_superuser
            user = form.save(commit=False)
            user.is_superuser = is_admin
            user.is_staff = is_admin
            user.save()
            
            # Crear o actualizar Usuario con is_admin
            usuario, created = Usuario.objects.get_or_create(usuario=user)
            usuario.is_admin = is_admin
            usuario.save()

            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'gestorUser/signUp.html', {'form': form})




def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def servicios(request):
    return render(request, 'servicios.html')



@login_required
def listar_usuarios(request):
    if request.user.is_superuser:  # Verificar si es admin
        usuarios = User.objects.all()
        return render(request, 'gestorUser/listar_usuarios.html', {'usuarios': usuarios})
    else:
        # Puedes manejar la lógica específica para usuarios no administradores aquí si es necesario
        return render(request, 'gestorUser/listar_usuarios.html')
    



@login_required
@admin_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    usuario.delete()
    return redirect('listar_usuarios')





@login_required
def editar_usuario(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST, instance=request.user)
        usuario_form = ExtendedUsuarioForm(request.POST, instance=request.user.usuario)

        if user_form.is_valid() and usuario_form.is_valid():
            user_form.save()
            usuario_form.save()
            return redirect('ver_perfil')
    else:
        user_form = UsuarioForm(instance=request.user)
        usuario_form = ExtendedUsuarioForm(instance=request.user.usuario)

    return render(request, 'gestorUser/editar_usuario.html', {'user_form': user_form, 'usuario_form': usuario_form})



@login_required
def ver_perfil(request):
    return render(request, 'gestorUser/ver_perfil.html', {'user': request.user})