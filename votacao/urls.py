from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'votacao'

urlpatterns = [
   path('', views.home, name='votacao'),
   path('votar/<int:turno_id>/', views.votar, name='votar'),
   path('dados_candidato/', views.dados_candidato, name='dados_candidato'),
   path('registrar_votacao/', views.registrar_votacao, name='registrar_votacao')
]