from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from votacao.models import Candidato, Turno, Eleicao, VotacaoTurnoCandidato, RegistroVotacao
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.db.models import Q

# Create your views here.
def home(request):
    title = 'Votação'

    """
        Eleições por turno por tipo

        Exibe eleições do estado de cadastro do eleitor e também eleições que não possuem estado associado (federais)

        Ao cadastrar um novo turno deve-se lembrar de cadastrar o resultado da eleição para cada candidato
    """

    data = {}

    eleicoes = Eleicao.objects.filter((Q(estado=request.user.estado) | Q(estado=None)), ano__gte=int(datetime.now().year))
    turnos = Turno.objects.filter(eleicao__in=(eleicoes), ativo=True)

    print(eleicoes)

    for eleicao in eleicoes:
        try:
            turnos_eleicao = Turno.objects.filter(eleicao=eleicao.id)
            color = ''
            font_color = ''

            for turno in turnos_eleicao:
                if (eleicao.get_tipo_display() == 'Presidente') or (eleicao.get_tipo_display() == 'Senadore') or (eleicao.get_tipo_display() == 'Deputado Federal'):
                    color = 'success'
                elif (eleicao.get_tipo_display() == 'Governador') or (eleicao.get_tipo_display() == 'Deputado estadual'):
                    color = 'danger'
                    
                
                data.update({
                    eleicao.id: {
                        'turno': turno.id,
                        'dat_ini': turno.dat_ini, 
                        'dat_fim': turno.dat_fim,
                        'tipo': eleicao.get_tipo_display(),
                        'color': color,
                    } 
                })
        
        except Turno.DoesNotExist:
            print('não contém turno')
        
    print(data)

    return render(request, 'votacao/home.html', {'title': title, 'eleicoes': data})

@login_required
def votar(request, turno_id=0):
    title = 'Votar'

    """
        Lista todas as informações para votação em eleição selecionada
    """

    if (turno_id == 0):
        return HttpResponseRedirect(reverse('votacao:inicio'))

    try:
        turno = Turno.objects.get(id=turno_id)
        registro = RegistroVotacao.objects.filter(usuario=request.user, turno=turno)
        eleicao = Eleicao.objects.get(id=turno.eleicao.id)

        candidatos = VotacaoTurnoCandidato.objects.filter(turno=turno)

        return render(request, 'votacao/votar.html', {'title': title, 'registro': registro, 'turno': turno, 'candidatos': candidatos, 'eleicao': eleicao})

    except Turno.DoesNotExist:
        return HttpResponseRedirect(reverse('votacao:inicio'))