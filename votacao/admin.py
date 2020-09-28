from django.contrib import admin
from votacao.models import Candidato, Eleicao, Turno

# Register your models here.
@admin.register(Eleicao)
class EleicaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'ano']
    list_filter = ['ano', 'tipo']
    search_fields = ['data']

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ['id', 'dat_ini', 'dat_fim']
    list_filter = ['dat_ini', 'dat_fim']
    search_fields = ['dat_ini', 'dat_fim']