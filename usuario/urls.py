from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [    
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo'),
    path('lista/', views.UsuarioList.as_view(), name='lista'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('signup/', views.SignupUsuario.as_view(), name='signup'),
     path('eliminar/<int:pk>', views.UsuarioDelete.as_view(), name='eliminar'),
    path('editar/<int:pk>', views.UsuarioActualizar.as_view(), name='editar'),
    path('logout/', views.logout_view, name='logout'),
    
]