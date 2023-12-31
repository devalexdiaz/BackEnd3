from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Usuario

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)
    is_admin = forms.BooleanField(required=False, initial=False)  # Nuevo campo

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_admin')



class UsuarioForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ExtendedUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('descripcion', 'sitioWeb')