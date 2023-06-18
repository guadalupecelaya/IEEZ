from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Usuario
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm, UsuarioFormLog
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
from django.views.generic import ListView, DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required



class NuevoUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'nuevo_user':True}
    success_url = reverse_lazy('usuario:lista')

    def form_valid(self, form):
        user = form.save(commit=False)
        # user.is_active = 0
        # print (user)
        return super().form_valid(form)
    
class UsuarioList( ListView):
    paginate_by = 10
    model = Usuario
    context_object_name = 'usuario'
    lista_grupos = Group.objects.all()
    extra_context={'us_lista':True}

def logout_view(request):
    logout(request)
    return redirect('usuario:login')

class LoginUsuario(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

class SignupUsuario(CreateView):
    template_name = 'signup.html'
    model = Usuario
    form_class = UsuarioFormLog
    #extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'nuevo_user':True}
    success_url = reverse_lazy('usuario:login')





# Create your views here.
class NuevoUsuario(CreateView):
    model = Usuario
    form_class = ('first_name','username','password','rfc')
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar'}
    success_url = reverse_lazy('usuario:lista')

    def form_valid(self, form):
        user = form.save(commit=False)
        return super().form_valid(form)

    
class UsuarioActualizar( UpdateView):
    model = Usuario
    fields = ('first_name','username','password','rfc')
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('usuario:lista')



class UsuarioDelete( DeleteView):
    model = Usuario
    extra_context = {'etiqueta':'Eliminar', 'user_del':True}
    success_url = reverse_lazy('usuario:lista')


def eliminar_usuario(id):
    Usuario = get_object_or_404(Usuario, id=id)
    Usuario.delete()

    return redirect('usuario:lista')


class UsuarioDetalle( DetailView):
    model = Usuario
    extra_context = {'etiqueta':'Detalles', 'boton':'Regresar'}


def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(instance=usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:lista')
    context = {'form': form }
    return render(request, 'editar_usuario.html', context) 