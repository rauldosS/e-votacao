from django.contrib import admin
from votacao.models import Candidato, Eleicao, Turno, VotacaoTurnoCandidato, RegistroVotacao

# Register your models here.
@admin.register(Eleicao)
class EleicaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'ano']
    list_filter = ['ano', 'tipo']
    search_fields = ['data']

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ['id', 'eleicao', 'dat_ini', 'dat_fim', 'ativo']
    list_filter = ['dat_ini', 'dat_fim']
    search_fields = ['dat_ini', 'dat_fim']

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'nascimento', 'titulo', 'estado', 'partido', 'numero']
    list_filter = ['nome', 'nascimento', 'titulo', 'estado', 'partido', 'numero']
    search_fields = ['nome', 'titulo', 'estado', 'partido']

@admin.register(VotacaoTurnoCandidato)
class VotacaoTurnoCandidato(admin.ModelAdmin):
    list_filter = ['id', 'candidato', 'turno']
    list_filter = ['candidato', 'turno']
    search_fields = ['candidato', 'turno']

@admin.register(RegistroVotacao)
class RegistroVotacaoAdmin(admin.ModelAdmin):
    list_filter = ['id', 'eleicao', 'turno', 'candidato', 'data']
    list_filter = ['candidato', 'turno']
    search_fields = ['candidato', 'turno', 'data', 'eleicao']