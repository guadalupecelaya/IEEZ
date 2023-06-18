from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.
class ProveedorList(ListView):
    #permission_required = 'auth.administrador_permiso'
    paginate_by = 10
    model = Proveedor
    context_object_name = 'proveedores'
    extra_context = {'etiqueta': 'Lista', 'mt_lista': True}

class ProveedorCrear( CreateView):
    model = Proveedor
    form_class = ProveedorForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar', 'mt_nuevo': True}
    success_url = reverse_lazy('proveedores:lista')