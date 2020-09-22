from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views 

app_name = 'controle'
title = 'Painel de controle'

urlpatterns = [
   path('', views.home, name='home')
]