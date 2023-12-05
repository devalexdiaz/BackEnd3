from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
from .models import Usuario
from .forms import SignUpForm
from .decorators import admin_required



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
            # Crear usuario como superuser si el checkbox está marcado
            user = form.save(commit=False)
            if is_admin:
                user.is_superuser = True
                user.is_staff = True
            user.save()
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'gestorUser/signUp.html', {'form': form})


""" Agregar el formulario de panel sb2 """
""" Agregar los campos faltantes que agregamos al modelo Usuario """


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