from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'resultado'

urlpatterns = [
   path('', views.home, name='resultado'),
]