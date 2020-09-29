from django.shortcuts import render
import requests
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from votacao.models import Candidato, Turno, Eleicao, VotacaoTurnoCandidato, RegistroVotacao
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.db.models import Q
# from django.contrib.auth.models import User
import json

module = 'Resultados'

# Create your views here.
@login_required
def home(request):
    title = 'Resultados'

    datas = get_resultados(request)

    return render(request, 'resultado/home.html', {'title': title, 'module': module, 'datas': datas})

def get_resultados(request):
    eleicoes = Eleicao.objects.all()
    turnos = Turno.objects.all()
    votacoesTurnosCandidatos = VotacaoTurnoCandidato.objects.all()

    dados = { } # turnos

    for eleicao in eleicoes:
        dados.update({
            eleicao.id : {
                'ano': eleicao.ano,
                'tipo': eleicao.get_tipo_display(),
                'estado': eleicao.estado if eleicao.estado else 'Presidente',
                'turnos': {}
            } 
        })
        
    for turno in turnos:
        dados[turno.eleicao.id]['turnos'].update({ 
                turno.turno: { }
            })

        for votacaoTurnoCandidato in votacoesTurnosCandidatos:
            
            if votacaoTurnoCandidato.turno.id == turno.id:
                print(votacaoTurnoCandidato.candidato.nome)

                dados[turno.eleicao.id]['turnos'][turno.turno].update({
                    votacaoTurnoCandidato.candidato.nome: votacaoTurnoCandidato.votos
                })

    return dados