from django.contrib import admin
from usuario.models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'fullname', 'cpf', 'rg', 'user_active']
    list_filter = ['user_active']
    search_fields = ['username', 'fullname']