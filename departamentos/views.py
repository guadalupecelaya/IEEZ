from django.shortcuts import render, redirect
from .models import Departamentos
from .forms import DepartamentoForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.

class DepartamentoList(ListView):
    #permission_required = 'auth.administrador_permiso'
    paginate_by = 10
    model = Departamentos
    context_object_name = 'departamentos'
    extra_context = {'etiqueta': 'Lista', 'mt_lista': True}

class DepartamentoCrear( CreateView):
    model = Departamentos
    form_class = DepartamentoForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar', 'dpto_nuevo': True}
    success_url = reverse_lazy('departamentos:lista')


class DepartamentoDelete( DeleteView):
    model = Departamentos
    extra_context = {'etiqueta':'Eliminar', 'user_del':True}
    success_url = reverse_lazy('departamentos:lista')

def eliminar_departamento(id):
    Departamentos = get_object_or_404(Departamentos, id=id)
    Departamentos.delete()

    return redirect('departamentos:lista')