from django.urls import include, path
from django.contrib.auth.decorators import login_required
from usuario.views import ListaUsuario, RegistrarUsuario, CadastroUsuario
from . import views

app_name = 'usuarios'

urlpatterns = [
   path('usuario/', views.home, name='dados'),
   path('listar_usuarios/', login_required(ListaUsuario.as_view()), name='listar_usuarios'),
   path('registrar_usuario/', login_required(RegistrarUsuario.as_view()), name='registrar_usuario'),
   path('cadastro_usuario/', CadastroUsuario.as_view(), name='cadastro_usuario')
]