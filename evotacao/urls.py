from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from face_detector import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('face_detection/detect/', views.detect),
    path('usuarios/', include('usuario.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('controle/', include('controle.urls')),
    path('', include('home.urls')),
]