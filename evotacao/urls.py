from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from face_detector import views
from django.contrib.staticfiles.urls import static

# app_name='evotacao'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('face_detection/detect/', views.detect),
    path('usuarios/', include('usuario.urls')),
    path('controle/', include('controle.urls')),
    path('votacao/', include('votacao.urls')),
    path('resultado/', include('resultado.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)