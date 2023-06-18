from django.urls import path
from . import views

app_name = 'departamentos'

urlpatterns = [
    path('lista/', views.DepartamentoList.as_view(), name='lista'),
    path('nuevo/', views.DepartamentoCrear.as_view(), name='nuevo'),
    path('eliminar/<int:pk>', views.DepartamentoDelete.as_view(), name='eliminar'),
    


]
