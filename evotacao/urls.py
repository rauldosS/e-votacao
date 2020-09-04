from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuario.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
]