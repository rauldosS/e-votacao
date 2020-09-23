from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views 

app_name = 'face_detector'

urlpatterns = [
   path('detect/', views.detect, name='detect')
]