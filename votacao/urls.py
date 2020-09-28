from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'votacao'

urlpatterns = [
   path('inicio/', views.home, name='inicio'),
   path('votar/<int:turno_id>/', views.votar, name='votar'),
]