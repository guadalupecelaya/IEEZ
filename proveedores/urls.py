from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('lista/', views.ProveedorList.as_view(), name='lista'),
    path('nuevo/', views.ProveedorCrear.as_view(), name='nuevo'),    
]
