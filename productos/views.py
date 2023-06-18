from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.

class ProductoList(ListView):
    #permission_required = 'auth.administrador_permiso'
    paginate_by = 10
    model = Producto
    context_object_name = 'productos'
    extra_context = {'etiqueta': 'Lista', 'mt_lista': True}

class ProductoCrear( CreateView):
    model = Producto
    form_class = ProductoForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar', 'mt_nuevo': True}
    success_url = reverse_lazy('productos:lista')
