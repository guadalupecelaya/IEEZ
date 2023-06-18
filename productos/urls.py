from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('lista/', views.ProductoList.as_view(), name='lista'),
    path('nuevo/', views.ProductoCrear.as_view(), name='nuevo'),
    


]
